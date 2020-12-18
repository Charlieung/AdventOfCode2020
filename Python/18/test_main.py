import pytest
from main import solve#, solve_two

# @pytest.fixture
# def expense_report():
#     return [1721, 979, 366, 299, 675, 1456]

def test_solve_1():
    input = '1 + 2 * 3 + 4 * 5 + 6'
    answer = solve(input)
    assert answer == 71

def test_solve_2():
    input = '1 + (2 * 3) + (4 * (5 + 6))'
    answer = solve(input)
    assert answer == 51

def test_solve_3():
    input = '2 * 3 + (4 * 5)'
    answer = solve(input)
    assert answer == 26

def test_solve_4():
    input = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
    answer = solve(input)
    assert answer == 437

def test_solve_5():
    input = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    answer = solve(input)
    assert answer == 12240

def test_solve_6():
    input = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    answer = solve(input)
    assert answer == 13632