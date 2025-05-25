from abc import ABC, abstractclassmethod
import pyttsx3, subprocess, os

from ..service import IService

class ISpeaker (ABC, IService):
    def __init__(self, driverName: str) -> None:
        self.__driver = pyttsx3.init()

    @abstractclassmethod
    def speak(self, message: str) -> None:
        raise NotImplementedError("abstart method class")

    @property
    def driver(self) -> object: return self.__driver


class DefaultSpeaker (ISpeaker):
    def speak(self, message: str) -> None:
        self.driver.say(message)
        self.driver.runAndWait()


class FileSpeaker (ISpeaker):
    TEMP_FILE_NAME: str = "temp.mp3"

    def __init__(self, driverName: str = "espeak", directory: str = ".") -> None:
        super().__init__(driverName)
        self._directory = directory

    def speak(self, message: str) -> None:
        filePath = f"{self._directory}/{self.TEMP_FILE_NAME}"
        self.driver.save_to_file(message, filePath)
        self.driver.runAndWait()

        subprocess.Popen(["aplay", f"{filePath}"])

AVAILABLE_DRIVERS: list[str] = ["espeak", "dummy"]
SPEAKER_TYPES = [FileSpeaker, DefaultSpeaker]

AVAILABLE_SPEAKERS: dict[str, ISpeaker] = {}

for index in range(len(AVAILABLE_DRIVERS)):
    try:
        AVAILABLE_SPEAKERS[AVAILABLE_DRIVERS[index]+f"_{index}"] = SPEAKER_TYPES[index](AVAILABLE_DRIVERS[index])
    except (RuntimeError, TypeError, ModuleNotFoundError):
        print("speaker is not available")
        continue

print(f"current availbale speakers: {AVAILABLE_SPEAKERS}")

def testSpeakers(message: str) -> None:
    try:
        for key, value in AVAILABLE_SPEAKERS.items():
            value.speak(message)
    except ... as error:
        print(error)

    print(f"tested: {AVAILABLE_SPEAKERS}")

if __name__ == "__main__" :
    print("testing speaking sybsystem... Result is written in logs.txt")
    testSpeakers("Hello world")


