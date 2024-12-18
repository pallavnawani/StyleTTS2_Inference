from styletts2 import tts

# No paths provided means default checkpoints/configs will be downloaded/cached.
#my_tts = tts.StyleTTS2()

# Optionally create/write an output WAV file.
#out = my_tts.inference("Hello there, I am now a python package.", output_wav_file="test.wav")

# Specific paths to a checkpoint and config can also be provided.
other_tts = tts.StyleTTS2(model_checkpoint_path='model/epochs_2nd_00020.pth', config_path='model/Models_LibriTTS_config.yml')

aVoiceStylePath = "voices/WomanGood1/WomanGood1.wav"
aVoiceStyle = other_tts.compute_style(aVoiceStylePath)
aTextToTTS = "Walks through the directory 'voices', looks for .wav and .mp3 files,"

# Specify target voice to clone. When no target voice is provided, a default voice will be used.
other_tts.inference(aTextToTTS, None, "results/another_test.wav",output_sample_rate=24000, alpha=0.3, beta=0.7, diffusion_steps=5, embedding_scale=1, ref_s=aVoiceStyle)
