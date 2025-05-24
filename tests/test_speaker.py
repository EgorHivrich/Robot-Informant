import sounddevice, torch, time

model, _ = torch.hub.load (
	repo_or_dir = "snakers4/silero-models",
	model = "silero_tts",
	language = "ru",
	speaker = "ru_v3"
)

model.to(torch.device("cpu"))

audio = model.apply_tts (
	text = "Привет мир",
	speaker = "kseniya",
	put_accent = True,
	put_yo = True,
	
	sample_rate = 48000
)

sounddevice.play(audio, samplerate = 48000)
time.sleep(len(audio) / 48000)

sounddevice.stop()
