import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (3, 2, 1),
    (-1, -1, 0),
    (0, 0, 0),
    (-5, 5, -10),
    (1.5, 2.5, -1.0),
    (1e10, 1e10, 0.0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_with_strings():
    with pytest.raises(TypeError):
        subtract('a', 'b')
