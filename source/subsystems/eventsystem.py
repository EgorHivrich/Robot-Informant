from enum import Enum
from typing import Callable

class Handler:
    def __init__(self, function: Callable, args: list[object]) -> None:
        self._function = function
        self._args = args

    def execute(self) -> None:
        self._function(*self._args) 

class Event:
    class EventType (Enum):
        VoiceMessage = 0,
        USBMessage = 1,
    
    _type: EventType = None
    _handler: Handler = None

    def __init__(self, type: EventType, handler: Handler) -> None:
        self._type = type
        self._handler = handler

    @property
    def handler(self) -> Handler:
        return self._handler

    @handler.setter
    def handler(self, handler: Handler) -> None:
        self._handler = handler

    def __str__(self) -> str: return str(self._type)

def bindEventHandler(event: Event) -> Callable:
    def wrapper(function: Callable) -> None:
        event.handler = Handler(function, [])
        function()
    return wrapper

def recognizeEventByName(name: str) -> Event.EventType:
    events = {
        "0": Event(0), "1": Event(1), "None": Event(None)
    }
    return events[name]