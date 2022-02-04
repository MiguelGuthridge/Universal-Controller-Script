
from common.types import eventData
from common.eventpattern import BasicEventPattern, fromNibbles
from . import ControlSurface, IValueStrategy

class NoteValueStrategy(IValueStrategy):
    def getValueFromEvent(self, event: eventData) -> int:
        if 0x80 <= event.status < 0x90:
            return 0
        else:
            return event.data2
    
    def getFloatFromValue(self, value: int) -> float:
        return value / 127
    
    def getValueFromFloat(self, f: float) -> int:
        return int(f * 127)

class Note(ControlSurface):
    
    def __init__(self, note_num: int, channel:int = 0) -> None:
        super().__init__(
            BasicEventPattern(fromNibbles((8, 9), channel), note_num, ...),
            NoteValueStrategy(),
            "notes",
            (channel, note_num)
        )

    @staticmethod
    def getControlAssignmentPriorities() -> 'tuple[type[ControlSurface], ...]':
        return tuple()