# Project Title

## Description

A brief description of the project.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
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
