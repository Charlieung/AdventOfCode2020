import pytest

from main import parse_input, solve_one, solve_two

@pytest.fixture
def c():
    input = """
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    """.strip().replace('    ', '')
    seat_layout = parse_input(input)
    return seat_layout

def test_solve_one(seat_layout):
    assert solve_one(seat_layout) == 35

def test_solve_two(seat_layout):
    assert solve_two(seat_layout) == 8