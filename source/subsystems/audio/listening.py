from speech_recognition import (
	Microphone, Recognizer
) 
from ..utility.connection import isThereInternetConnection

def listenAndRecognizeSpeech() -> str:
    try:
        with Microphone() as microphone:
            recognizer = Recognizer()
            return recognizer.recognize_google(recognizer.listen(microphone)).lower()

    except Exception as error: return error

if isThereInternetConnection().isAvailable == True:
	print("connection is available now")
else:
	print("connection isn`t available now cannot recognize speech")
