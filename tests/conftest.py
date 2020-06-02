"""Conftest.py is loaded for each pytest. Contains fixtures shared by multiple tests
"""
import pytest


@pytest.fixture
def shared_fixture():
    """Sample pytest fixture that can be used from within any pytest in this folder

    """
    return 'A shared value'
