from typing import Callable, dataclass_transform
from pyttsx3 import init, Engine

from speech_recognition import 

from requests import get

class MessageInfo:
    def __init__(self, text: str, attributes: list[dict[str, object]]) -> None:
        self.text = text
        self.attributes = attributes

    text: str = ""
    attributes: list[dict[str, object]] = [ ]

    def __str__(self) -> str: return self.text

class Speaker:
    _driver: Engine = init()

    def setupDriverAttributes(self, attributes: list[dict[str, object]]) -> None: 
        for attribute in attributes:
            self._driver.setProperty(attribute.keys(), attribute.values())
        
        print("current attributes: " + attributes)

    def speak(self, message: MessageInfo) -> None:
        self.setupDriverAttributes(message.attributes)

        self._driver.say(message)
        self._driver.runAndWait()

    def __init__(self, language: str) -> None: self.setupDriverAttributes([{"voice", language}])

class SpeechRecognizer:
    _recognitionMethod: Callable = None

    def recordAndRecognizeSpeech(self) -> MessageInfo:
        return self._recognitionMethod()
        
    def recognizeSpeechOnline(self) -> MessageInfo:

class UsbController:
    def __init__(self, vendorID: int, productID: int) -> None:
        pass