from datetime import datetime

class FileLogger:
    def __new__(self, *args, **kwargs) -> None:
        if not self._instance:
            self._instance = super(FileLogger, self).__new__(self, *args, **kwargs)
        return self._instance

    def __init__(self, filePath: str = "./logs.txt") -> None:
        self._filePath = filePath

class InternetLogger (FileLogger): pass