import sys
sys.path.insert(1, "../source")

from subsystems.audio.listening import listenAndRecognizeSpeech

text = listenAndRecognizeSpeech()
print(f"text: {text}")

