from datetime import datetime
from abc import ABC, abstractmethod

import yagmail, json

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
			with open(self._filePath, "w") as file:
				for i in args:
					file.write(f"{datetime.now()}: {i}\n")
			return True
		except ... as error: return False
	
	@property
	def filePath(self) -> str: return _filePath
	
	@filePath.setter
	def filePath(self, filePath: str) -> None: self._filePath = filePath
	
	_filePath: str = "./logs.txt"
	
	
class JsonLoggingKind (TextLoggingKind):
	def logData(self, *args, **kwargs) -> bool:
		return super().logData(json.dumps(args))
		
	_filePath: str = "./logs.json"
		
		
class EmailLoggingKind (ILoggingKind):
	def __init__(self, sender: str, destination: str) -> None:
		self._client = yagmail.SMTP(sender, "asiy nydw ebbo eryh")
		self._destination = destination
		
	def logData(self, *args, **kwargs) -> bool:
		try:
			content = ""
			for i in args:
				content += f"{i}\n"
				
			self._client.send (
				self._destination,
				self.MESSAGE_HEADER.format(datetime.now),
				content
			)
			return True
		
		except ... as error: return False
		
	MESSAGE_HEADER: str = "LOGGING ERRORS: {0}"
