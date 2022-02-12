
from typing import Any
import ui
import playlist
import transport
import general
from common.extensionmanager import ExtensionManager
from common.util.apifixes import UnsafeIndex, getSelectedPlaylistTrack
from controlsurfaces import consts
from controlsurfaces import ControlShadow
from controlsurfaces import MoveJogWheel, StandardJogWheel, JogWheel
from devices import DeviceShadow
from plugs import WindowPlugin

INDEX = 2

class Playlist(WindowPlugin):
    """
    Used to process events as a fallback if there isn't a plugin registered for
    the active FL plugin.
    
    Handles:
    * Pedals
    * Mod and pitch wheels
    * Notes
    """
    def __init__(self, shadow: DeviceShadow) -> None:
        shadow.bindMatches(JogWheel, self.jogWheel, raise_on_failure=False)
        super().__init__(shadow, [])
    
    @staticmethod
    def getWindowId() -> int:
        return INDEX
    
    @classmethod
    def create(cls, shadow: DeviceShadow) -> 'WindowPlugin':
        return cls(shadow)

    def jogWheel(self, control: ControlShadow, index: UnsafeIndex, *args: Any) -> bool:
        if control.getCurrentValue() == consts.ENCODER_NEXT:
            increment = 1
        elif control.getCurrentValue() == consts.ENCODER_PREV:
            increment = -1
        elif control.getCurrentValue() == consts.ENCODER_SELECT:
            ui.enter()
            return True
        else:
            return True
        
        if isinstance(control.getControl(), StandardJogWheel):
            # Scroll through tracks
            track = getSelectedPlaylistTrack() + increment
            if track <= 0:
                track = 1
            elif track >= 500:
                track = playlist.trackCount() - 1
            playlist.deselectAll()
            playlist.selectTrack(track)
            ui.scrollWindow(INDEX, track)
        elif isinstance(control.getControl(), MoveJogWheel):
            # Need to account for ticks being zero-indexed and bars being
            # 1-indexed
            bar = int(transport.getSongPos(3)) + increment - 1
            ui.scrollWindow(INDEX, bar, 1)
            # TODO: Make this work with time signature markers
            transport.setSongPos(bar * general.getRecPPB(), 2)
        return True

ExtensionManager.registerWindowPlugin(Playlist)