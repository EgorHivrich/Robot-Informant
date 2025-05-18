from subsystems.eventsystem import bindEventHandler, Event

event = Event(Event.EventType.VoiceMessage, None)

@bindEventHandler(event=event)
def handler() -> None:
    print("Hello world")

print(event.handler != None)