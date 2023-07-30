import playlist
from common.types import Color
from .abstract import AbstractTrack


class PlaylistTrack(AbstractTrack):
    """
    Helper class for accessing properties of playlist tracks
    """

    def __init__(self, index: int) -> None:
        self.__index = index

    @property
    def color(self) -> Color:
        return Color.fromInteger(playlist.getTrackColor(self.__index))

    @color.setter
    def color(self, new_color: Color) -> None:
        playlist.setTrackColor(self.__index, new_color.integer)

    @property
    def name(self) -> str:
        return playlist.getTrackName(self.__index)

    @name.setter
    def name(self, new_name: str) -> None:
        playlist.setTrackName(self.__index, new_name)

    @name.setter
    def name(self, new_name: str) -> None:
        playlist.setTrackName(self.__index, new_name)

    @property
    def mute(self) -> bool:
        return playlist.isTrackMuted(self.__index)

    @mute.setter
    def mute(self, new_value: bool) -> None:
        if new_value != self.mute:
            playlist.muteTrack(self.__index)

    def muteToggle(self) -> None:
        playlist.muteTrack(self.__index)

    @property
    def solo(self) -> bool:
        return playlist.isTrackSolo(self.__index)

    @solo.setter
    def solo(self, new_value: bool) -> None:
        if new_value != self.solo:
            playlist.soloTrack(self.__index)

    def soloToggle(self) -> None:
        playlist.soloTrack(self.__index)