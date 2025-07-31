"""
Tests for CLI functionality
"""

import pytest
from unittest.mock import patch


class TestCLICommands:
    """Test CLI command parsing and execution"""

    @patch("sys.argv", ["automashupper", "--version"])
    def test_version_command(self, capsys):
        """Test --version command"""
        from auto_mashupper.cli import main

        with pytest.raises(SystemExit) as excinfo:
            main()

        # Should exit with code 0 for version
        assert excinfo.value.code == 0

    @patch("sys.argv", ["automashupper", "--help"])
    def test_help_command(self, capsys):
        """Test --help command"""
        from auto_mashupper.cli import main

        with pytest.raises(SystemExit) as excinfo:
            main()

        # Should exit with code 0 for help
        assert excinfo.value.code == 0

    @patch("sys.argv", ["automashupper"])
    def test_no_arguments(self, capsys):
        """Test CLI with no arguments"""
        from auto_mashupper.cli import main

        with pytest.raises(SystemExit) as excinfo:
            main()

        # Should exit with code 1 for missing arguments
        assert excinfo.value.code == 1


class TestCLIMashabilityCommand:
    """Test mashability CLI command"""

    @patch("sys.argv", ["automashupper", "mashability"])
    @patch("sys.argv", ["automashupper", "mashability"])
    def test_mashability_command_no_args(self, capsys):
        """Test mashability command without arguments"""
        from auto_mashupper.cli import main

        with pytest.raises(SystemExit):
            main()

    @patch("sys.argv", ["automashupper", "mashability", "test_song.mp3"])
    def test_mashability_command_with_file(self, capsys):
        """Test mashability command with file argument"""
        from auto_mashupper.cli import main

        with pytest.raises(SystemExit):
            main()

    @patch("sys.argv", ["automashupper", "mashability", "nonexistent.mp3"])
    def test_mashability_command_missing_dependencies(self, capsys):
        """Test mashability command when dependencies are missing"""
        # Mock the import to fail
        with patch.dict("sys.modules", {"auto_mashupper.mashability": None}):
            from auto_mashupper.cli import main

            with pytest.raises(SystemExit) as excinfo:
                main()

            assert excinfo.value.code == 1
            captured = capsys.readouterr()
            assert "dependencies not available" in captured.err.lower()


class TestCLIGenerateCommand:
    """Test generate CLI command"""

    @patch("sys.argv", ["automashupper", "generate", "test_song.mp3"])
    @patch("pathlib.Path.exists", return_value=True)
    def test_generate_command_valid_file(self, mock_exists, capsys):
        """Test generate command with valid file"""
        from auto_mashupper.cli import main

        with pytest.raises(SystemExit):
            main()

    @patch("sys.argv", ["automashupper", "generate", "nonexistent.mp3"])
    @patch("pathlib.Path.exists", return_value=False)
    def test_generate_command_missing_file(self, mock_exists, capsys):
        """Test generate command with missing file"""
        from auto_mashupper.cli import main

        with pytest.raises(SystemExit) as excinfo:
            main()

        assert excinfo.value.code == 1
        # Either file not found or dependency error is expected
        captured = capsys.readouterr()
        assert "not found" in captured.err or "Error:" in captured.err

    @patch("sys.argv", ["automashupper", "generate", "test_song.mp3"])
    @patch("pathlib.Path.exists", return_value=True)
    def test_generate_command_missing_dependencies(self, mock_exists, capsys):
        """Test generate command when dependencies are missing"""
        # Mock the import to fail
        with patch.dict("sys.modules", {"auto_mashupper.mashability": None}):
            from auto_mashupper.cli import main

            with pytest.raises(SystemExit) as excinfo:
                main()

            assert excinfo.value.code == 1
            captured = capsys.readouterr()
            assert "dependencies not available" in captured.err.lower()


class TestCLIErrorHandling:
    """Test CLI error handling"""

    @patch("sys.argv", ["automashupper", "invalid_command"])
    def test_invalid_command(self):
        """Test CLI with invalid command"""
        from auto_mashupper.cli import main

        with pytest.raises(SystemExit) as excinfo:
            main()

        assert excinfo.value.code == 2

    @patch("sys.argv", ["automashupper", "generate"])
    def test_generate_missing_argument(self):
        """Test generate command without required file argument"""
        from auto_mashupper.cli import main

        with pytest.raises(SystemExit):
            main()


@pytest.mark.integration
class TestCLIIntegration:
    """Integration tests for CLI functionality"""

    def test_cli_module_structure(self):
        """Test that CLI module has expected structure"""
        from auto_mashupper import cli

        assert hasattr(cli, "main")
        assert callable(cli.main)

    @pytest.mark.dependency
    def test_import_cli_dependencies(self):
        """Test that CLI can import its dependencies"""
        try:
            from auto_mashupper.cli import main

            # If this succeeds, basic imports work
            assert main is not None
        except ImportError as e:
            pytest.skip(f"CLI dependencies not available: {e}")

    def test_cli_argument_parser_setup(self):
        """Test that argument parser is set up correctly"""
        from auto_mashupper.cli import main

        # This tests that the argument parser doesn't crash on setup
        # We can't easily test the actual parser without mocking sys.argv
        # but we can ensure the function exists and is callable
        assert callable(main)
