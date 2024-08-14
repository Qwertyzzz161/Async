import pytest
from task1 import find_divisors


def test_find_divisors():
    number = 3250000
    expected_output = [1, 2, 4, 5, 8, 10, 13, 16, 20, 25, 26, 40, 50,
                       52, 65, 80, 100, 104, 125, 130, 200, 208, 250, 260,
                       325, 400, 500, 520, 625, 650, 1000, 1040, 1250, 1300,
                       1625, 2000, 2500, 2600, 3125, 3250, 5000, 5200, 6250,
                       6500, 8125, 10000, 12500, 13000, 15625, 16250, 25000,
                       26000, 31250, 32500, 40625, 50000, 62500, 65000, 81250,
                       125000, 130000, 162500, 203125, 250000, 325000, 406250,
                       650000, 812500, 1625000, 3250000]

    assert find_divisors(number) == expected_output, f"Expected {expected_output}, got {find_divisors(number)}"
