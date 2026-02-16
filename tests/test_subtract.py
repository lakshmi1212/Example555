import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (-1, -1, 0),
    (0, 0, 0),
    (200, 100, 100),
    (-5, 5, -10),
    (2.5, 1.5, 1.0),
    (1e10, 1e9, 9e9)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
