from attr import Factory
import pytest

from main import parse_input, solve_one, solve_two

@pytest.fixture
def initial_state():
    input = """
    .#.
    ..#
    ###
    """.strip().replace('    ', '')
    initial_state = parse_input(input)
    return initial_state

def test_solve_one(initial_state):
    cycles = 6
    result = solve_one(initial_state, cycles)
    assert result == 112

# def test_solve_two(initial_state):
#     cycles = 6
#     result = solve_two(initial_state, cycles)
#     assert result == 112