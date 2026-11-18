import pytest

from calc import average


def test_average() -> None:
    """平均が正しく計算されることを確かめる。"""
    assert average([1, 2, 3]) == 2
    assert average([1, 2]) == 1.5


def test_average_empty() -> None:
    """空のリストでは ValueError になることを確かめる。"""
    with pytest.raises(ValueError):
        average([])
