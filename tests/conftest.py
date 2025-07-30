"""
Configuration for pytest
"""

import pytest
import numpy as np


@pytest.fixture(scope="session")
def sample_audio_short():
    """Session-wide fixture for short audio sample"""
    np.random.seed(42)  # For reproducible tests
    return np.random.random(1000)


@pytest.fixture(scope="session")
def sample_audio_medium():
    """Session-wide fixture for medium audio sample"""
    np.random.seed(42)  # For reproducible tests
    return np.random.random(22050)  # 0.5 seconds at 44.1kHz


@pytest.fixture(scope="session")
def sample_audio_long():
    """Session-wide fixture for long audio sample"""
    np.random.seed(42)  # For reproducible tests
    return np.random.random(44100)  # 1 second at 44.1kHz


@pytest.fixture
def sample_bpm_values():
    """Fixture providing common BPM values for testing"""
    return [60, 90, 120, 140, 180]


def pytest_configure(config):
    """Pytest configuration"""
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests (may be slow)"
    )
    config.addinivalue_line(
        "markers", "dependency: marks tests that require all dependencies"
    )
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (may take several seconds)"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test names"""
    for item in items:
        # Add integration marker to tests with 'integration' in name
        if "integration" in item.name.lower():
            item.add_marker(pytest.mark.integration)

        # Add dependency marker to tests that likely need all deps
        if any(
            keyword in item.name.lower()
            for keyword in ["mashability", "generation", "workflow"]
        ):
            item.add_marker(pytest.mark.dependency)
