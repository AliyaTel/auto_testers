import pytest
from utils import get_max, get_min, get_average


def test_get_max():
    assert get_max([1, 5, 3]) == 5
    assert get_max([-10, -3, -20]) == -3

    with pytest.raises(ValueError):
        get_max([])


def test_get_min():
    assert get_min([4, 2, 9]) == 2
    assert get_min([-5, -1, -9]) == -9

    with pytest.raises(ValueError):
        get_min([])


def test_get_average():
    assert get_average([2, 4, 6]) == 4
    assert get_average([1]) == 1
    assert get_average([-3, 3]) == 0

    with pytest.raises(ValueError):
        get_average([])
