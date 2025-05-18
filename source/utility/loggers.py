from datetime import datetime
from abc import ABC, abstractmethod 

import yagmail

class ILoggingKind (ABC):
	@abstractmethod
	def logData(self, *args, **kwargs) -> bool:
		raise NotImplemented()

	_isDisabled: bool = False

class Logger: 
	@property
	def loggingKind(self) -> list[ILoggingKind]: return _loggingKind
		
	@loggingKind.setter
	def loggingKind(self, kinds: list[ILoggingKind]) -> None:
		for item in kinds:
			self._loggingKind.append(item)
		return self._loggingKind
			
	_loggingKind: list[ILoggingKind] = [ ]

class TextLoggingKind (ILoggingKind):
	def __init__(self, filePath: str) -> None:
		self._filePath = filePath
	
	def logData(self, *args, **kwargs) -> bool:
		try:
			with open(self._filePath) as file:
				file.write(map(lambda x: f"{datetime.now()}: {x}\n"))
			return True
		except: return False
	
	@property
	def filePath(self) -> str: return _filePath
	
	_filePath: str = "./logs.txt"
	
class JsonLoggingKind (ILoggingKind, TextLoggingKind):
	def logData(self, *args, **kwargs) -> bool:
		try:
			with open(self.filePath) as file:
				file.write(json.dumbs(**kwargs))
			return True
		except: return False
