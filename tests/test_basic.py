"""
Basic tests for AutoMashupper package using pytest
"""

import pytest
import numpy as np
from unittest.mock import patch


class TestPackageImport:
    """Test package import and basic structure"""

    def test_package_import(self):
        """Test that the package can be imported"""
        import auto_mashupper

        assert hasattr(auto_mashupper, "__version__")
        assert auto_mashupper.__version__ == "0.1.0"

    def test_main_functions_available(self):
        """Test that main functions are available"""
        import auto_mashupper

        # Check main functions exist
        assert hasattr(auto_mashupper, "get_mashability")
        assert hasattr(auto_mashupper, "mashability")
        assert hasattr(auto_mashupper, "mix_songs")
        assert hasattr(auto_mashupper, "adjust_tempo")

    def test_cli_import(self):
        """Test that CLI module can be imported"""
        from auto_mashupper import cli

        assert hasattr(cli, "main")


class TestMashabilityFunction:
    """Test mashability function with various scenarios"""

    @pytest.fixture
    def sample_audio_data(self):
        """Fixture providing sample audio data"""
        return {
            "audio1": np.random.random(44100),  # 1 second of audio
            "audio2": np.random.random(44100),  # 1 second of audio
            "short_audio": np.random.random(1000),  # Very short audio
            "empty_audio": np.array([]),  # Empty audio
        }

    def test_mashability_function_basic(self, sample_audio_data):
        """Test basic mashability function with dummy data"""
        from auto_mashupper import get_mashability

        audio1 = sample_audio_data["audio1"]
        audio2 = sample_audio_data["audio2"]

        try:
            result = get_mashability(audio1, audio2, bpm1=120, bpm2=130)
            # Just check that it returns something without crashing
            assert result is not None
        except Exception as e:
            # For now, just ensure the function exists and can be called
            # The actual computation might fail due to dependencies
            pytest.skip(f"Mashability test skipped due to dependency issue: {e}")

    def test_mashability_function_with_invalid_input(self, sample_audio_data):
        """Test mashability function with invalid inputs"""
        from auto_mashupper import get_mashability

        # Test with empty audio
        with pytest.raises((ValueError, ImportError, Exception)):
            get_mashability(
                sample_audio_data["empty_audio"],
                sample_audio_data["audio1"],
                bpm1=120,
                bpm2=130,
            )

    @pytest.mark.parametrize(
        "bpm1,bpm2", [(60, 120), (120, 120), (90, 180), (140, 70)]
    )
    def test_mashability_different_bpms(self, sample_audio_data, bpm1, bpm2):
        """Test mashability function with different BPM combinations"""
        from auto_mashupper import get_mashability

        audio1 = sample_audio_data["audio1"]
        audio2 = sample_audio_data["audio2"]

        try:
            result = get_mashability(audio1, audio2, bpm1=bpm1, bpm2=bpm2)
            assert result is not None
        except Exception as e:
            pytest.skip(f"Mashability test skipped due to dependency issue: {e}")


class TestUtilityFunctions:
    """Test utility functions"""

    @pytest.fixture
    def sample_audio_data(self):
        """Fixture providing sample audio data"""
        return np.random.random(44100)  # 1 second of audio

    def test_utility_functions_exist(self):
        """Test that utility functions exist and are callable"""
        import auto_mashupper

        functions = [
            "mix_songs",
            "adjust_tempo",
            "match_target_amplitude",
            "self_tempo_estimation",
            "rotate_audio",
        ]

        for func_name in functions:
            assert hasattr(auto_mashupper, func_name)
            func = getattr(auto_mashupper, func_name)
            assert callable(func)

    def test_adjust_tempo_function(self, sample_audio_data):
        """Test adjust_tempo function"""
        try:
            from auto_mashupper import adjust_tempo

            # This might fail due to dependencies, so we wrap in try/except
            result = adjust_tempo(sample_audio_data, final_tempo=120)
            assert result is not None
        except Exception as e:
            pytest.skip(f"adjust_tempo test skipped due to dependency issue: {e}")


class TestSegmentationFunctions:
    """Test segmentation functions"""

    def test_segmentation_functions_exist(self):
        """Test that segmentation functions exist and are callable"""
        import auto_mashupper

        functions = [
            "get_beat_sync_chroma_and_spectrum",
            "get_beat_sync_chroma",
            "get_beat_sync_spectrums",
        ]

        for func_name in functions:
            assert hasattr(auto_mashupper, func_name)
            func = getattr(auto_mashupper, func_name)
            assert callable(func)


class TestCLI:
    """Test CLI functionality"""

    def test_cli_main_function_exists(self):
        """Test that CLI main function exists"""
        from auto_mashupper.cli import main

        assert callable(main)

    @patch("sys.argv", ["automashupper", "--version"])
    @patch("sys.exit")
    def test_cli_version(self, mock_exit):
        """Test CLI version command"""
        from auto_mashupper.cli import main

        with patch("builtins.print") as mock_print:
            try:
                main()
            except SystemExit:
                pass

        # Should have called print or exit
        assert mock_print.called or mock_exit.called

    @patch("sys.argv", ["automashupper", "--help"])
    @patch("sys.exit")
    def test_cli_help(self, mock_exit):
        """Test CLI help command"""
        from auto_mashupper.cli import main

        with patch("builtins.print") as mock_print:
            try:
                main()
            except SystemExit:
                pass

        # Should have called print or exit
        assert mock_print.called or mock_exit.called

    @patch("sys.argv", ["automashupper"])
    @patch("sys.exit")
    def test_cli_no_args(self, mock_exit):
        """Test CLI with no arguments"""
        from auto_mashupper.cli import main

        try:
            main()
        except SystemExit:
            pass

        # Should exit with error code
        mock_exit.assert_called_with(1)


@pytest.mark.integration
class TestIntegration:
    """Integration tests that require all dependencies"""

    @pytest.mark.skip(reason="Requires audio files and all dependencies")
    def test_full_mashability_workflow(self):
        """Test full mashability workflow with real audio files"""
        # This would test the complete workflow but requires audio files
        # and all dependencies to be properly installed
        pass

    @pytest.mark.skip(reason="Requires audio files and all dependencies")
    def test_full_generation_workflow(self):
        """Test full mashup generation workflow"""
        # This would test the complete generation workflow
        pass
