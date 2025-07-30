"""
AutoMashupper - Automatic mashup generator using audio analysis and beat matching
"""

__version__ = "0.1.0"

# Lazy import helpers
def _get_mashability_functions():
    """Lazy import of mashability functions"""
    try:
        from .mashability import get_mashability, mashability, main as mashability_main
        return get_mashability, mashability, mashability_main
    except ImportError as e:
        raise ImportError(f"Mashability functions not available: {e}")

def _get_segmentation_functions():
    """Lazy import of segmentation functions"""
    try:
        from .segmentation import (
            get_beat_sync_chroma_and_spectrum,
            get_beat_sync_chroma,
            get_beat_sync_spectrums,
        )
        return get_beat_sync_chroma_and_spectrum, get_beat_sync_chroma, get_beat_sync_spectrums
    except ImportError as e:
        raise ImportError(f"Segmentation functions not available: {e}")

def _get_utility_functions():
    """Lazy import of utility functions"""
    try:
        from .utilities import (
            mix_songs,
            adjust_tempo,
            match_target_amplitude,
            self_tempo_estimation,
            rotate_audio,
        )
        return mix_songs, adjust_tempo, match_target_amplitude, self_tempo_estimation, rotate_audio
    except ImportError as e:
        raise ImportError(f"Utility functions not available: {e}")

# Expose functions with lazy loading
def get_mashability(*args, **kwargs):
    """Calculate mashability between two audio vectors"""
    get_mashability_func, _, _ = _get_mashability_functions()
    return get_mashability_func(*args, **kwargs)

def mashability(*args, **kwargs):
    """Calculate mashability with beat sync chroma features"""
    _, mashability_func, _ = _get_mashability_functions()
    return mashability_func(*args, **kwargs)

def mashability_main(*args, **kwargs):
    """Main mashability CLI function"""
    _, _, main_func = _get_mashability_functions()
    return main_func(*args, **kwargs)

def get_beat_sync_chroma_and_spectrum(*args, **kwargs):
    """Get beat synchronized chroma and spectrum features"""
    func, _, _ = _get_segmentation_functions()
    return func(*args, **kwargs)

def get_beat_sync_chroma(*args, **kwargs):
    """Get beat synchronized chroma features"""
    _, func, _ = _get_segmentation_functions()
    return func(*args, **kwargs)

def get_beat_sync_spectrums(*args, **kwargs):
    """Get beat synchronized spectrums"""
    _, _, func = _get_segmentation_functions()
    return func(*args, **kwargs)

def mix_songs(*args, **kwargs):
    """Mix two songs with tempo and pitch adjustment"""
    func, _, _, _, _ = _get_utility_functions()
    return func(*args, **kwargs)

def adjust_tempo(*args, **kwargs):
    """Adjust tempo of audio"""
    _, func, _, _, _ = _get_utility_functions()
    return func(*args, **kwargs)

def match_target_amplitude(*args, **kwargs):
    """Match target amplitude of audio"""
    _, _, func, _, _ = _get_utility_functions()
    return func(*args, **kwargs)

def self_tempo_estimation(*args, **kwargs):
    """Estimate tempo of audio"""
    _, _, _, func, _ = _get_utility_functions()
    return func(*args, **kwargs)

def rotate_audio(*args, **kwargs):
    """Rotate audio by number of beats"""
    _, _, _, _, func = _get_utility_functions()
    return func(*args, **kwargs)

# Export the main functions
__all__ = [
    "__version__",
    "get_mashability",
    "mashability", 
    "mashability_main",
    "get_beat_sync_chroma_and_spectrum",
    "get_beat_sync_chroma",
    "get_beat_sync_spectrums",
    "mix_songs",
    "adjust_tempo",
    "match_target_amplitude", 
    "self_tempo_estimation",
    "rotate_audio",
]