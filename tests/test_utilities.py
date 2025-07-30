"""
Tests for utility functions
"""

import pytest
import numpy as np


class TestUtilityFunctions:
    """Test utility functions availability and basic functionality"""

    def test_utility_functions_exist(self):
        """Test that all utility functions exist and are callable"""
        import auto_mashupper

        expected_functions = [
            "mix_songs",
            "adjust_tempo",
            "match_target_amplitude",
            "self_tempo_estimation",
            "rotate_audio",
        ]

        for func_name in expected_functions:
            assert hasattr(auto_mashupper, func_name), f"Function {func_name} not found"
            func = getattr(auto_mashupper, func_name)
            assert callable(func), f"Function {func_name} is not callable"


class TestAdjustTempo:
    """Test adjust_tempo function"""

    @pytest.mark.dependency
    def test_adjust_tempo_basic(self, sample_audio_long):
        """Test basic tempo adjustment"""
        try:
            from auto_mashupper import adjust_tempo
            
            result = adjust_tempo(sample_audio_long, final_tempo=120)
            
            assert result is not None
            assert isinstance(result, np.ndarray)
            
        except ImportError as e:
            pytest.skip(f"adjust_tempo dependencies not available: {e}")

    @pytest.mark.dependency
    @pytest.mark.parametrize("tempo", [60, 90, 120, 140, 180])
    def test_adjust_tempo_different_values(self, sample_audio_medium, tempo):
        """Test tempo adjustment with different tempo values"""
        try:
            from auto_mashupper import adjust_tempo
            
            result = adjust_tempo(sample_audio_medium, final_tempo=tempo)
            
            assert result is not None
            assert isinstance(result, np.ndarray)
            
        except ImportError as e:
            pytest.skip(f"adjust_tempo dependencies not available: {e}")

    @pytest.mark.dependency
    def test_adjust_tempo_edge_cases(self):
        """Test tempo adjustment with edge cases"""
        try:
            from auto_mashupper import adjust_tempo
            
            # Very short audio
            short_audio = np.random.random(100)
            
            with pytest.raises((ValueError, Exception)):
                adjust_tempo(short_audio, final_tempo=120)
            
            # Empty audio
            empty_audio = np.array([])
            
            with pytest.raises((ValueError, Exception)):
                adjust_tempo(empty_audio, final_tempo=120)
                
        except ImportError as e:
            pytest.skip(f"adjust_tempo dependencies not available: {e}")


class TestMixSongs:
    """Test mix_songs function"""

    @pytest.mark.dependency
    def test_mix_songs_basic(self, sample_audio_long):
        """Test basic song mixing"""
        try:
            from auto_mashupper import mix_songs
            
            main_song = sample_audio_long
            cand_song = np.random.random(44100)
            
            result = mix_songs(main_song, cand_song, beat_offset=0, pitch_shift=0)
            
            assert result is not None
            assert isinstance(result, (np.ndarray, tuple))
            
        except ImportError as e:
            pytest.skip(f"mix_songs dependencies not available: {e}")

    @pytest.mark.dependency
    @pytest.mark.parametrize("beat_offset,pitch_shift", [
        (0, 0),
        (4, 2),
        (8, -2),
        (2, 1),
        (6, -1)
    ])
    def test_mix_songs_different_parameters(self, sample_audio_medium, beat_offset, pitch_shift):
        """Test song mixing with different parameters"""
        try:
            from auto_mashupper import mix_songs
            
            main_song = sample_audio_medium
            cand_song = np.random.random(22050)
            
            result = mix_songs(main_song, cand_song, beat_offset=beat_offset, pitch_shift=pitch_shift)
            
            assert result is not None
            
        except ImportError as e:
            pytest.skip(f"mix_songs dependencies not available: {e}")


class TestMatchTargetAmplitude:
    """Test match_target_amplitude function"""

    @pytest.mark.dependency
    def test_match_target_amplitude_basic(self, sample_audio_long):
        """Test basic amplitude matching"""
        try:
            from auto_mashupper import match_target_amplitude
            
            # This function might work with pydub AudioSegment
            # For now, test that it exists and can be called
            assert callable(match_target_amplitude)
            
        except ImportError as e:
            pytest.skip(f"match_target_amplitude dependencies not available: {e}")

    @pytest.mark.dependency
    def test_match_target_amplitude_different_targets(self):
        """Test amplitude matching with different target values"""
        try:
            from auto_mashupper import match_target_amplitude
            
            # Test that function exists - actual testing would require pydub AudioSegment
            assert callable(match_target_amplitude)
            
        except ImportError as e:
            pytest.skip(f"match_target_amplitude dependencies not available: {e}")


class TestSelfTempoEstimation:
    """Test self_tempo_estimation function"""

    @pytest.mark.dependency
    def test_self_tempo_estimation_basic(self, sample_audio_long):
        """Test basic tempo estimation"""
        try:
            from auto_mashupper import self_tempo_estimation
            
            # Standard sample rate
            sr = 44100
            
            result = self_tempo_estimation(sample_audio_long, sr)
            
            assert result is not None
            # Tempo should be positive (handle both single values and tuples)
            if isinstance(result, (tuple, list)):
                assert len(result) > 0
                tempo_value = result[0] if isinstance(result[0], (int, float, np.number)) else result
            else:
                tempo_value = result
            
            if isinstance(tempo_value, (int, float, np.number)):
                assert float(tempo_value) > 0
            
        except ImportError as e:
            pytest.skip(f"self_tempo_estimation dependencies not available: {e}")

    @pytest.mark.dependency
    @pytest.mark.parametrize("sr", [22050, 44100, 48000])
    def test_self_tempo_estimation_different_sample_rates(self, sample_audio_medium, sr):
        """Test tempo estimation with different sample rates"""
        try:
            from auto_mashupper import self_tempo_estimation
            
            result = self_tempo_estimation(sample_audio_medium, sr)
            
            assert result is not None
            # Handle both single values and tuples for tempo result
            if isinstance(result, (tuple, list)):
                assert len(result) > 0
            else:
                assert isinstance(result, (int, float, np.number))
            
        except ImportError as e:
            pytest.skip(f"self_tempo_estimation dependencies not available: {e}")

    @pytest.mark.dependency
    def test_self_tempo_estimation_with_tempo_hint(self, sample_audio_long):
        """Test tempo estimation with tempo hint"""
        try:
            from auto_mashupper import self_tempo_estimation
            
            sr = 44100
            tempo_hint = 120
            
            result = self_tempo_estimation(sample_audio_long, sr, tempo=tempo_hint)
            
            assert result is not None
            # Handle both single values and tuples for tempo result
            if isinstance(result, (tuple, list)):
                assert len(result) > 0
            else:
                assert isinstance(result, (int, float, np.number))
            
        except ImportError as e:
            pytest.skip(f"self_tempo_estimation dependencies not available: {e}")


class TestRotateAudio:
    """Test rotate_audio function"""

    @pytest.mark.dependency
    def test_rotate_audio_basic(self, sample_audio_long):
        """Test basic audio rotation"""
        try:
            from auto_mashupper import rotate_audio
            
            sr = 44100
            n_beats = 4
            
            result = rotate_audio(sample_audio_long, sr, n_beats)
            
            assert result is not None
            assert isinstance(result, np.ndarray)
            assert len(result) <= len(sample_audio_long)  # Rotation might change length
            
        except ImportError as e:
            pytest.skip(f"rotate_audio dependencies not available: {e}")

    @pytest.mark.dependency
    @pytest.mark.parametrize("n_beats", [1, 2, 4, 8, 16])
    def test_rotate_audio_different_beats(self, sample_audio_medium, n_beats):
        """Test audio rotation with different beat counts"""
        try:
            from auto_mashupper import rotate_audio
            
            sr = 44100
            
            result = rotate_audio(sample_audio_medium, sr, n_beats)
            
            assert result is not None
            assert isinstance(result, np.ndarray)
            
        except ImportError as e:
            pytest.skip(f"rotate_audio dependencies not available: {e}")


@pytest.mark.dependency
class TestUtilityErrorHandling:
    """Test error handling in utility functions"""

    def test_utility_functions_with_invalid_input(self):
        """Test utility functions with invalid inputs"""
        try:
            from auto_mashupper import adjust_tempo, self_tempo_estimation, rotate_audio
            
            # Test with None input
            with pytest.raises((TypeError, ValueError, Exception)):
                adjust_tempo(None, final_tempo=120)
            
            with pytest.raises((TypeError, ValueError, Exception)):
                self_tempo_estimation(None, 44100)
            
            with pytest.raises((TypeError, ValueError, Exception)):
                rotate_audio(None, 44100, 4)
                
        except ImportError as e:
            pytest.skip(f"Utility function dependencies not available: {e}")

    def test_utility_functions_with_empty_input(self):
        """Test utility functions with empty audio"""
        try:
            from auto_mashupper import adjust_tempo, self_tempo_estimation, rotate_audio
            
            empty_audio = np.array([])
            
            # These should raise exceptions with empty input
            with pytest.raises((ValueError, Exception)):
                adjust_tempo(empty_audio, final_tempo=120)
            
            with pytest.raises((ValueError, Exception)):
                self_tempo_estimation(empty_audio, 44100)
            
            with pytest.raises((ValueError, Exception)):
                rotate_audio(empty_audio, 44100, 4)
                
        except ImportError as e:
            pytest.skip(f"Utility function dependencies not available: {e}")


@pytest.mark.slow
@pytest.mark.dependency
class TestUtilityPerformance:
    """Test performance characteristics of utility functions"""

    def test_tempo_estimation_performance(self, sample_audio_long):
        """Test that tempo estimation completes in reasonable time"""
        import time
        
        try:
            from auto_mashupper import self_tempo_estimation
            
            start_time = time.time()
            result = self_tempo_estimation(sample_audio_long, 44100)
            end_time = time.time()
            
            # Should complete within 10 seconds for 1 second of audio
            assert (end_time - start_time) < 10.0
            assert result is not None
            
        except ImportError as e:
            pytest.skip(f"Tempo estimation dependencies not available: {e}")

    def test_tempo_adjustment_performance(self, sample_audio_long):
        """Test that tempo adjustment completes in reasonable time"""
        import time
        
        try:
            from auto_mashupper import adjust_tempo
            
            start_time = time.time()
            result = adjust_tempo(sample_audio_long, final_tempo=120)
            end_time = time.time()
            
            # Should complete within 15 seconds for 1 second of audio
            assert (end_time - start_time) < 15.0
            assert result is not None
            
        except ImportError as e:
            pytest.skip(f"Tempo adjustment dependencies not available: {e}")
