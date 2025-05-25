from socket import (
	gethostbyname, create_connection
)
from dataclasses import dataclass
import platform, subprocess

@dataclass
class ConnectionInfo:
	isAvailable: bool
	ping: int
	
	serverName: str

	def __str__(self) -> str: return f"""
		is there connection?: {self.isAvailable}\n
		current ping to {self.serverName}: {self.speed}
	"""
	
SERVER_NAME = "www.google.com"	
	
def pingServer(serverName: str) -> int:
	return subprocess.call(["ping", "-n", "1", serverName])
	
def isThereInternetConnection() -> ConnectionInfo:
	try:
		socket = create_connection((SERVER_NAME, 80), 2).close()
		return ConnectionInfo(True, 160, SERVER_NAME)
		
	except: return ConnectionInfo(False, 0, SERVER_NAME)
		
