from typing import Callable
from enum import Enum

class Event:
    class EventType (Enum):
        VoiceMessage = 0,
        USBMessage = 1,
    
    _messageType: EventType = None
    
    def __init__(self, type: EventType) -> None:
        self._messageType = type

    def __str__(self) -> str: return str(self._messageType)


class BaseHandler:
    def __init__(self, function: Callable, args: list[object]) -> None:
        self._function = function
        self._args = args

    def execute(self) -> None:
        self._function(*self._args) 


def bindEvent(function: Callable, event: Event, handler: BaseHandler) -> Callable:
    def wrapper() -> None:
        handler.execute([])
        function()
    return wrapper

def recognizeEventByName(name: str) -> Event:
    events = {
        "0": Event(0), "1": Event(1), "None": Event(None)
    }
    return events[name]