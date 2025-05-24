from speech_recognition import (
	Microphone, Recognizer
) 
import sys
sys.path.insert(1, "/home/admin/Robot-Informant/source")

from utility.connection import isThereInternetConnection

def listenAndRecognizeSpeech() -> str:
	with Microphone() as microphone:
		recognizer = Recognizer()
		text = recognizer.listen(microphone)
	try:
		return recognizer.recognize_google(text)
	except Exception as error: return error

if isThereInternetConnection().isAvailable == True:
	print("connection is available now")
else:
	print("connection isn`t available now cannot recognize speech")
