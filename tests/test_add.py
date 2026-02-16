import pytest
from src.math_operations import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0),
    (-5, 5, 0),
    (1.5, 2.5, 4.0),
    (1e10, 1e10, 2e10),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_add_with_strings():
    with pytest.raises(TypeError):
        add('a', 'b')
