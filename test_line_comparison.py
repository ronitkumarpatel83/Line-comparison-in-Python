from main import Comparison
import pytest


@pytest.fixture
def comparison():
    return Comparison()


class TestLineComparison:
    def test_cartesian_length(self, comparison):
        x1 = 1
        y1 = 2
        x2 = 3
        y2 = 4
        a = comparison.cartesian_length(x1, x2, y1, y2)
        assert round(a, 1) == 2.8

    def test_equality_of_length(self, comparison):
        x3 = 5
        y3 = 6
        x4 = 7
        y4 = 8
        b = comparison.equality_of_length(x3, x4, y3, y4)
        assert round(b, 1) == 2.8
