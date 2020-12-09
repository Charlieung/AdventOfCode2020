import pytest

from main import parse_input, solve_one, solve_two

@pytest.fixture
def transmission():
    input = """
    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
    """.strip().replace('    ', '')
    transmission = parse_input(input)
    return transmission

def test_solve_one(transmission):
    window = 5
    assert solve_one(transmission, window) == 127

def test_solve_two(transmission):
    number = 127
    assert solve_two(transmission, number) == 62
