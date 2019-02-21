import python_template
import pytest


@pytest.mark.parametrize("value,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_calculate_square(value, expected):
    assert python_template.calculate_square(value) == expected
