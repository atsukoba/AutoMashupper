# AutoMashupper

Automatic mashup generator using audio analysis and beat matching.

Based on [AutoMashUpper: Automatic Creation of Multi-Song Music Mashups](https://www.researchgate.net/publication/265130656_AutoMashUpper_Automatic_Creation_of_Multi-Song_Music_Mashups)

## Features

- Audio analysis and beat synchronization
- Automatic mashability calculation between songs
- Tempo adjustment and pitch shifting
- Command-line interface for easy usage
- Python API for integration with other projects

## Installation

### From source (development)

```bash
# Clone the repository
git clone https://github.com/atsukoba/AutoMashupper.git
cd AutoMashupper

# Install in editable mode
pip install -e .
```

### System Dependencies

This package requires several system-level audio libraries:

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg libsndfile1 libfftw3-dev
```

**macOS:**
```bash
brew install ffmpeg fftw
```

**Windows:**
```bash
# Use conda for easier dependency management
conda install -c conda-forge ffmpeg
```

## Usage

### Command Line Interface

```bash
# Calculate mashability between songs
automashupper mashability base_song.mp3

# Generate a mashup
automashupper generate base_song.mp3

# Show version
automashupper --version
```

### Python API

```python
import auto_mashupper
from librosa import load

# Load audio files
audio1, sr1 = load("song1.mp3")
audio2, sr2 = load("song2.mp3")

# Calculate mashability
score = auto_mashupper.get_mashability(audio1, audio2, bpm1=120, bpm2=130)
print(f"Mashability score: {score}")

# Get beat-synchronized chroma features
chroma, spectrum = auto_mashupper.get_beat_sync_chroma_and_spectrum(audio1)

# Mix songs with tempo adjustment
mixed = auto_mashupper.mix_songs(audio1, audio2, beat_offset=0, pitch_shift=2)
```

## Development

### Setting up development environment

```bash
# Install UV (fast Python package manager)
pip install uv

# Install dependencies
uv sync --dev

# Install in editable mode
uv pip install -e .

# Run tests
uv run pytest tests/

# Run linting
uv run flake8 auto_mashupper
```

### Building the package

```bash
# Build wheel and source distribution
python -m build

# Check the distribution
python -m twine check dist/*
```

## Dependencies

- Python 3.9+
- librosa - Audio analysis
- numpy - Numerical computations
- scipy - Scientific computing
- essentia - Music analysis
- madmom - Music signal processing
- pyrubberband - Audio time-stretching and pitch-shifting
- pydub - Audio file manipulation
- matplotlib - Plotting

## License

MIT License

## Citation

If you use this code in your research, please cite:

```
AutoMashUpper: Automatic Creation of Multi-Song Music Mashups
```
