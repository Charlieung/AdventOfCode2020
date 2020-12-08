import pytest

from main import solve_one, solve_two

@pytest.fixture
def boot_code():
    input = """
    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6
    """.strip().replace('    ', '')
    return input

@pytest.fixture
def boot_code_alt():
    input = """
    jmp +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    nop -4
    acc +6
    """.strip().replace('    ', '')
    return input

def test_solve_one(boot_code):
    assert solve_one(boot_code) == 5

def test_solve_two(boot_code):
    assert solve_two(boot_code) == 8

def test_solve_two_2(boot_code_alt):
    assert solve_two(boot_code_alt) == 8
