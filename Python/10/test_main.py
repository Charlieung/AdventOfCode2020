import pytest

from main import parse_input, solve_one, solve_two

@pytest.fixture
def adapters():
    input = """
    16
    10
    15
    5
    1
    11
    7
    19
    6
    12
    4
    """.strip().replace('    ', '')
    adapters = parse_input(input)
    return adapters

@pytest.fixture
def larger_adapters():
    input = """
    28
    33
    18
    42
    31
    14
    46
    20
    48
    47
    24
    23
    49
    45
    19
    38
    39
    11
    1
    32
    25
    35
    8
    17
    7
    9
    4
    2
    34
    10
    3
    """.strip().replace('    ', '')
    adapters = parse_input(input)
    return adapters

def test_solve_one(adapters):
    assert solve_one(adapters) == 35

def test_solve_one_larger(larger_adapters):
    assert solve_one(larger_adapters) == 220

def test_solve_two(adapters):
    assert solve_two(adapters) == 8

def test_solve_two_larger(larger_adapters):
    assert solve_two(larger_adapters) == 19208