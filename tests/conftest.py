import pytest
from pathlib import Path


@pytest.fixture
def test_data():
    return Path(__file__).parent / "test_data" / "images"
