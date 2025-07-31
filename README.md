# AutoMashupper

Automatic mashup generator using audio analysis and beat matching.

Based on [AutoMashUpper: Automatic Creation of Multi-Song Music Mashups](https://www.researchgate.net/publication/265130656_AutoMashUpper_Automatic_Creation_of_Multi-Song_Music_Mashups)

> [!IMPORTANT]
> The original implementation repository is <https://github.com/migperfer/AutoMashupper>.

## Installation

Clone the repository

```bash
git clone https://github.com/atsukoba/AutoMashupper.git --recursive
```

and install deps

```bash
uv sync

# need to install mandom from source using pip
cd madmom
uv pip install -e .
```

### Dependencies

- Python 3.9
- librosa - Audio analysis
- numpy - Numerical computations
- scipy - Scientific computing
- essentia - Music analysis
- madmom - Music signal processing
- pyrubberband - Audio time-stretching and pitch-shifting
- pydub - Audio file manipulation
- matplotlib - Plotting


This package requires several system-level audio libraries:

**Ubuntu/Debian:**

```bash
sudo apt-get install ffmpeg libsndfile1 libfftw3-dev libeigen3-dev pkg-config
```

## Library

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

## License

MIT License

## Citation

Cite the originall paper and impelmentation.
