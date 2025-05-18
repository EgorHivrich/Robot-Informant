from datetime import datetime
import json

class FileLogger:
    _messages: list[str] = []
    
    def __init__(self, filePath: str = "./logs.txt") -> None:
        self._filePath = filePath
