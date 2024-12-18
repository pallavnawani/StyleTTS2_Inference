# Project Title
StyleTTS2 Package Inference

## Description

A Couple of python scripts to infer with the StyleTTS2 Package (https://github.com/sidharthrajaram/StyleTTS2).

## Installation

0. Create a Venv
   ``` python -m envtts2
   envtts2\Scripts\activate.bat
   ```
   
2. ```pip install styletts2
   ```
3. ```[Optional] Downloaded the StyleTTS2 LibriTTS checkpoint and corresponding config file. Both are available to download at https://huggingface.co/yl4579/StyleTTS2-LibriTTS. You can also provide paths to your own checkpoint and config file (just ensure it is the same format as the original one).
   ```

4. Clone the repository:
   ```bash
   git clone https://github.com/pallavnawani/StyleTTS2_Inference
   ```

## Usage

### Basic Inference

To perform basic text-to-speech inference using a single voice, run the `infer_basic.py` script:

```bash
python infer_basic.py
```

This script will generate an audio file named `another_test.wav` in the `results` directory, using the voice style from `voices/WomanGood1/WomanGood1.wav`.

### CSV-Based Inference

To perform text-to-speech inference using a CSV file for multiple voices and texts, run the `infer_csv.py` script:

```bash
python infer_csv.py
```

This script will read the `tts_input.csv` file, and for each row, it will generate an audio file in the `results` directory, using the voice style specified in the `SpeakerID` column. The script will look for voice files in the `voices` directory.

## Contributing

Guidelines for contributing to the project.

## License

Information about the project's license.