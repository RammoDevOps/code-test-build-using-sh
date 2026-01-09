import pytest
from utils import is_disk_usage_high

def test_disk_usage_below_threshold():
    assert is_disk_usage_high(50) is False

def test_disk_usage_equal_threshold():
    assert is_disk_usage_high(80) is True

def test_disk_usage_above_threshold():
    assert is_disk_usage_high(95) is True

def test_invalid_type():
    with pytest.raises(ValueError):
        is_disk_usage_high("90")

def test_invalid_range():
    with pytest.raises(ValueError):
        is_disk_usage_high(150)
