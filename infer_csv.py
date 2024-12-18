import os
import csv
from styletts2 import tts

# No paths provided means default checkpoints/configs will be downloaded/cached.
#my_tts = tts.StyleTTS2()

# Optionally create/write an output WAV file.
#out = my_tts.inference("Hello there, I am now a python package.", output_wav_file="test.wav")

# Specific paths to a checkpoint and config can also be provided.
other_tts = tts.StyleTTS2(model_checkpoint_path='model/epochs_2nd_00020.pth', config_path='model/Models_LibriTTS_config.yml')

# Create the 'results' directory if it doesn't exist
results_dir = 'results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

def load_voice_paths(directory):
    voice_paths = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav') or file.endswith('.mp3'):
                file_name = os.path.splitext(file)[0]
                file_path = str(os.path.join(root, file))
                voice_paths[file_name] = { "path": file_path, "ref_s": None }
    return voice_paths

def print_voice_paths(voice_paths):
    for key, value in voice_paths.items():
        key_utf8 = key.encode('utf-8').decode('utf-8')
        value_utf8 = {k: (v.encode('utf-8').decode('utf-8') if isinstance(v, str) else v) for k, v in value.items()}
        print(f"{key_utf8}: {value_utf8}")

def load_tts_input(csv_file):
    data = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

voice_paths = load_voice_paths('voices')
print_voice_paths(voice_paths)

tts_data = load_tts_input('tts_input.csv')
for row in tts_data:
    output_name = row['OutputName']
    speaker_id = row['SpeakerID']
    text = row['Text']

    output_path = str(os.path.join(results_dir, f"{output_name}.wav")).encode('utf-8').decode('utf-8')
    aTextToTTS = text

    if speaker_id in voice_paths:
        if voice_paths[speaker_id]['ref_s'] is not None:
            aVoiceStyle = voice_paths[speaker_id]['ref_s']
        else:
            voice_path = voice_paths[speaker_id]['path']
            aVoiceStyle = other_tts.compute_style(voice_path)
            voice_paths[speaker_id]['ref_s'] = aVoiceStyle

        # Print statement displaying the text being inferred and the speakerID
        print(f"Inferring text: '{aTextToTTS}' with speakerID: '{speaker_id}'")

        # Specify target voice to clone. When no target voice is provided, a default voice will be used.
        #other_tts.inference(aTextToTTS, None, output_path, output_sample_rate=24000, alpha=0.3, beta=0.7, diffusion_steps=5, embedding_scale=1, ref_s=aVoiceStyle)
        other_tts.inference(aTextToTTS, None, output_path, output_sample_rate=24000, alpha=0.7, beta=0.3, diffusion_steps=3, embedding_scale=1, ref_s=aVoiceStyle)
    else:
        print(f"SpeakerID {speaker_id} not found in voice_paths")
