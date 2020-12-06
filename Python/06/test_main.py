import pytest
from main import solve_one, solve_two

@pytest.fixture
def declaration_forms():
    input = """
    abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b
    """.strip().replace('    ', '')
    return input

def test_solve_one(declaration_forms):
    assert solve_one(declaration_forms) == 11

def test_solve_two(declaration_forms):
    assert solve_two(declaration_forms) == 6