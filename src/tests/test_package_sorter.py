import pytest
from package_sorter import sort


def test_standard_package():
    """Test standar packages"""
    # Small and light
    assert sort(10, 20, 30, 5) == "STANDARD"
    # Maximum
    assert sort(99.9999, 99.999, 99.999, 19.9999) == "STANDARD"


def test_special():
    """Test packages that are special"""
    # Just heavy
    assert sort(10, 20, 30, 20) == "SPECIAL"
    assert sort(10, 20, 30, 20.0000000000000001) == "SPECIAL"
    # Just bulk
    assert sort(200, 200, 200, 1) == "SPECIAL"
    assert sort(1, 1, 200, 1) == "SPECIAL"
    assert sort(1, 200, 1, 1) == "SPECIAL"
    assert sort(200, 1, 1, 1) == "SPECIAL"


def test_rejected_package():
    """Test packages that should be rejeted"""
    assert sort(100, 100, 100, 20) == "REJECTED"
    assert sort(150, 10, 10, 20) == "REJECTED"
    assert sort(150, 150, 150, 20) == "REJECTED"


def test_invalid_inputs():
    """Test invalid input values and types"""
    # Negative
    with pytest.raises(ValueError):
        sort(-1, 10, 10, 10)
    # Zero
    with pytest.raises(ValueError):
        sort(0, 10, 10, 10)
    # Non-numeric input
    with pytest.raises(ValueError):
        sort("10", 10, 10, 10)
