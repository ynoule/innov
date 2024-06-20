import pytest
from average import calculate_average

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([-1, 1, -1, 1]) == 0
    assert calculate_average([]) == 0

if __name__ == "__main__":
    pytest.main()

