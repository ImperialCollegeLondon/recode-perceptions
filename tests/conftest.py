from pathlib import Path

import pytest


@pytest.fixture
def test_data():
    return Path(__file__).parent / "test_input/test_images"


@pytest.fixture
def root_dir():
    return Path(__file__).parent.parent


@pytest.fixture
def study():
    return "50a68a51fdc9f05596000002"


@pytest.fixture
def params():
    return {
        "batch_size": 1,
        "shuffle": True,
        "num_workers": 1,
        "pin_memory": True,
        "drop_last": False,
    }


# def pytest_addoption(parser):
#     parser.addoption("--root_dir", action="store")

# @pytest.fixture
# def name(request):
#     name_value = request.config.option.name
#     if name_value is None:
#         pytest.skip()
#     return name_value
