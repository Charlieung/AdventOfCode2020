import pytest
from main import solve_equation_one, solve_equation_two

# @pytest.fixture
# def expense_report():
#     return [1721, 979, 366, 299, 675, 1456]

def test_solve_one_1():
    input = '1 + 2 * 3 + 4 * 5 + 6'
    answer = solve_equation_one(input)
    assert answer == 71

def test_solve_one_2():
    input = '1 + (2 * 3) + (4 * (5 + 6))'
    answer = solve_equation_one(input)
    assert answer == 51

def test_solve_one_3():
    input = '2 * 3 + (4 * 5)'
    answer = solve_equation_one(input)
    assert answer == 26

def test_solve_one_4():
    input = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
    answer = solve_equation_one(input)
    assert answer == 437

def test_solve_one_5():
    input = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    answer = solve_equation_one(input)
    assert answer == 12240

def test_solve_one_6():
    input = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    answer = solve_equation_one(input)
    assert answer == 13632

def test_solve_two_1():
    input = '1 + 2 * 3 + 4 * 5 + 6'
    answer = solve_equation_two(input)
    assert answer == 231

def test_solve_two_2():
    input = '1 + (2 * 3) + (4 * (5 + 6))'
    answer = solve_equation_two(input)
    assert answer == 51

def test_solve_two_3():
    input = '2 * 3 + (4 * 5)'
    answer = solve_equation_two(input)
    assert answer == 46

def test_solve_two_4():
    input = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
    answer = solve_equation_two(input)
    assert answer == 1445

def test_solve_two_5():
    input = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    answer = solve_equation_two(input)
    assert answer == 669060

def test_solve_two_6():
    input = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    answer = solve_equation_two(input)
    assert answer == 23340