from subsystems.audio import (
    listening, speaking
)    

def main() -> None:
    commands = {
        "привет": "Hello",
        "пока": "Good bye"
    }

    speaker = speaking.DefaultSpeaker("espeak")
    command = listening.listenAndRecognizeSpeech()
    
    speaker.speak(command)

if __name__ == "__main__":
    main() 
