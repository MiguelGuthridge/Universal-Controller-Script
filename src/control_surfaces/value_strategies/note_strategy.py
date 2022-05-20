"""
controlsurfaces > valuestrategies > ntoestrategy

Contains the definition for the note value strategy

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]
"""
from common.types import EventData
from common.types.event_data import isEventStandard
from . import IValueStrategy


class NoteStrategy(IValueStrategy):
    """
    The strategy to get data values from note events
    """

    def getValueFromEvent(self, event: EventData, value: float) -> float:
        assert isEventStandard(event)
        if 0x80 <= event.status < 0x90:
            return 0.0
        else:
            return event.data2 / 127

    def getChannelFromEvent(self, event: EventData) -> int:
        assert isEventStandard(event)
        return event.status & 0xF