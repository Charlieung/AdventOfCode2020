import pytest

from main import parse_input, solve_one, solve_two

@pytest.fixture
def instructions():
    input = """
    F10
    N3
    F7
    R90
    F11
    """.strip().replace('    ', '')
    instructions = parse_input(input)
    return instructions

def test_solve_one(instructions):
    assert solve_one(instructions) == 25

def test_solve_two(instructions):
    assert solve_two(instructions) == 286