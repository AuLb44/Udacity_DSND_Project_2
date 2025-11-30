"""
Tests for dashboard ML visualization generation.

This module tests the ML visualization functionality including
the plot_ml_performance function and image file generation.
"""
import pytest
from pathlib import Path
import sys

# Add the report directory to path so we can import utils
project_root = Path(__file__).resolve().parent.parent
report_dir = project_root / 'report'
sys.path.insert(0, str(report_dir))


@pytest.fixture
def temp_output_path(tmp_path):
    """Create a temporary directory for test outputs."""
    return tmp_path / 'ml_performance.png'


@pytest.fixture
def sample_dept_counts():
    """Provide sample department counts for testing."""
    return {
        'Engineering': 45,
        'Sales': 32,
        'Marketing': 28,
        'Support': 38,
        'HR': 15
    }


def test_ml_visualization_generation(temp_output_path, sample_dept_counts):
    """
    Test that plot_ml_performance generates an ML PNG file.

    This test calls the visualization generation and asserts
    the ML PNG file exists after generation.
    """
    from utils import plot_ml_performance

    # Generate the ML visualization
    plot_ml_performance(sample_dept_counts, temp_output_path)

    # Assert the file was created
    assert temp_output_path.is_file(), "ML performance PNG file was not created"

    # Assert file is not empty
    assert temp_output_path.stat().st_size > 0, "ML performance PNG file is empty"
