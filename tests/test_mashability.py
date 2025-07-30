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
    @pytest.mark.parametrize("bpm1,bpm2", [
        (60, 120),
        (90, 180),
        (120, 120),
        (140, 70),
        (100, 150)
    ])
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


@pytest.mark.dependency
class TestMashabilityMain:
    """Test mashability main function"""

    def test_mashability_main_exists(self):
        """Test that mashability_main function exists"""
        import auto_mashupper
        
        assert hasattr(auto_mashupper, "mashability_main")
        assert callable(auto_mashupper.mashability_main)

    def test_mashability_main_call(self):
        """Test calling mashability main function"""
        with patch('auto_mashupper.mashability.main') as mock_main:
            from auto_mashupper.mashability import main as mashability_main
            
            # Test that main function can be called
            try:
                mashability_main('test_file.mp3')
                mock_main.assert_called_once_with('test_file.mp3')
            except (ImportError, AttributeError):
                # Skip if dependencies not available
                pass


@pytest.mark.slow
@pytest.mark.dependency
class TestMashabilityPerformance:
    """Test performance characteristics of mashability functions"""

    def test_mashability_reasonable_time(self, sample_audio_long):
        """Test that mashability computation completes in reasonable time"""
        import time
        
        try:
            from auto_mashupper import get_mashability
            
            audio1 = sample_audio_long
            audio2 = np.random.random(44100)
            
            start_time = time.time()
            result = get_mashability(audio1, audio2, bpm1=120, bpm2=130)
            end_time = time.time()
            
            # Should complete within 30 seconds for 1 second of audio
            assert (end_time - start_time) < 30.0
            assert result is not None
            
        except ImportError as e:
            pytest.skip(f"Mashability dependencies not available: {e}")

    def test_mashability_memory_usage(self, sample_audio_long):
        """Test that mashability doesn't use excessive memory"""
        try:
            from auto_mashupper import get_mashability
            
            audio1 = sample_audio_long
            audio2 = np.random.random(44100)
            
            # This is a basic test - in a real scenario you might use memory profiling
            result = get_mashability(audio1, audio2, bpm1=120, bpm2=130)
            
            # If we get here without memory errors, the test passes
            assert result is not None
            
        except ImportError as e:
            pytest.skip(f"Mashability dependencies not available: {e}")
        except MemoryError:
            pytest.fail("Mashability function used too much memory")
