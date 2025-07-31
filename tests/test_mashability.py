"""
Tests for mashability functions
"""

import pytest
import numpy as np
from unittest.mock import patch


class TestMashabilityCore:
    """Test core mashability functionality"""

    def test_get_mashability_function_exists(self):
        """Test that get_mashability function exists"""
        import auto_mashupper

        assert hasattr(auto_mashupper, "get_mashability")
        assert callable(auto_mashupper.get_mashability)

    def test_mashability_function_exists(self):
        """Test that mashability function exists"""
        import auto_mashupper

        assert hasattr(auto_mashupper, "mashability")
        assert callable(auto_mashupper.mashability)

    @pytest.mark.dependency
    def test_get_mashability_with_valid_input(self, sample_audio_long):
        """Test get_mashability with valid audio input"""
        try:
            from auto_mashupper import get_mashability

            audio1 = sample_audio_long
            audio2 = np.random.random(44100)

            result = get_mashability(audio1, audio2, bpm1=120, bpm2=130)

            # Should return a numeric value
            assert isinstance(result, (int, float, np.number))
            assert not np.isnan(result)

        except ImportError as e:
            pytest.skip(f"Mashability dependencies not available: {e}")

    @pytest.mark.dependency
    @pytest.mark.parametrize(
        "bpm1,bpm2", [(60, 120), (90, 180), (120, 120), (140, 70), (100, 150)]
    )
    def test_get_mashability_different_bpms(self, sample_audio_long, bpm1, bpm2):
        """Test get_mashability with different BPM combinations"""
        try:
            from auto_mashupper import get_mashability

            audio1 = sample_audio_long
            audio2 = np.random.random(44100)

            result = get_mashability(audio1, audio2, bpm1=bpm1, bpm2=bpm2)
            assert result is not None

        except ImportError as e:
            pytest.skip(f"Mashability dependencies not available: {e}")

    @pytest.mark.dependency
    def test_get_mashability_edge_cases(self):
        """Test get_mashability with edge cases"""
        try:
            from auto_mashupper import get_mashability

            # Very short audio
            short_audio1 = np.random.random(100)
            short_audio2 = np.random.random(100)

            with pytest.raises((ValueError, Exception)):
                get_mashability(short_audio1, short_audio2, bpm1=120, bpm2=130)

            # Empty audio
            empty_audio = np.array([])
            normal_audio = np.random.random(44100)

            with pytest.raises((ValueError, Exception)):
                get_mashability(empty_audio, normal_audio, bpm1=120, bpm2=130)

        except ImportError as e:
            pytest.skip(f"Mashability dependencies not available: {e}")


class TestMashabilityErrorHandling:
    """Test error handling in mashability functions"""

    def test_get_mashability_invalid_bpm(self, sample_audio_long):
        """Test get_mashability with invalid BPM values"""
        try:
            from auto_mashupper import get_mashability

            audio1 = sample_audio_long
            audio2 = np.random.random(44100)

            # Negative BPM
            with pytest.raises((ValueError, Exception)):
                get_mashability(audio1, audio2, bpm1=-10, bpm2=120)

            # Zero BPM
            with pytest.raises((ValueError, Exception)):
                get_mashability(audio1, audio2, bpm1=0, bpm2=120)

            # Extremely high BPM
            with pytest.raises((ValueError, Exception)):
                get_mashability(audio1, audio2, bpm1=1000, bpm2=1000)

        except ImportError as e:
            pytest.skip(f"Mashability dependencies not available: {e}")

    def test_get_mashability_wrong_input_type(self):
        """Test get_mashability with wrong input types"""
        try:
            from auto_mashupper import get_mashability

            # String instead of array
            with pytest.raises((TypeError, ValueError, Exception)):
                get_mashability("not_an_array", "also_not_an_array", bpm1=120, bpm2=130)

            # None values
            with pytest.raises((TypeError, ValueError, Exception)):
                get_mashability(None, None, bpm1=120, bpm2=130)

        except ImportError as e:
            pytest.skip(f"Mashability dependencies not available: {e}")
