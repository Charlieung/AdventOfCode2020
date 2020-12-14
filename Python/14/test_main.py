import pytest

from main import parse_input, solve_one, solve_two

@pytest.fixture
def instructions_one():
    input = """
    mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0
    """.strip().replace('    ', '')
    instructions = parse_input(input)
    return instructions

@pytest.fixture
def instructions_two():
    input = """
    mask = 000000000000000000000000000000X1001X
    mem[42] = 100
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1
    """.strip().replace('    ', '')
    instructions = parse_input(input)
    return instructions

def test_solve_one(instructions_one):
    result = solve_one(instructions_one)
    assert result == 165

def test_solve_two(instructions_two):
    result = solve_two(instructions_two)
    assert result == 208