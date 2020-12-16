import pytest

from main import parse_input, solve_one, solve_two

def test_solve_one_1():
    input = """
    0,3,6
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_one(starting_numbers, 2020)
    assert result == 436

def test_solve_one_2():
    input = """
    1,3,2
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_one(starting_numbers, 2020)
    assert result == 1

def test_solve_one_3():
    input = """
    2,1,3
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_one(starting_numbers, 2020)
    assert result == 10

def test_solve_one_4():
    input = """
    1,2,3
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_one(starting_numbers, 2020)
    assert result == 27

def test_solve_one_5():
    input = """
    2,3,1
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_one(starting_numbers, 2020)
    assert result == 78

def test_solve_one_6():
    input = """
    2,3,1
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_one(starting_numbers, 2020)
    assert result == 78

def test_solve_one_7():
    input = """
    3,2,1
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_one(starting_numbers, 2020)
    assert result == 438

def test_solve_one_8():
    input = """
    3,1,2
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_one(starting_numbers, 2020)
    assert result == 1836

def test_solve_two_1():
    input = """
    0,3,6
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_two(starting_numbers, 30000000)
    assert result == 175594

def test_solve_two_2():
    input = """
    1,3,2
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_two(starting_numbers, 30000000)
    assert result == 2578

def test_solve_two_3():
    input = """
    2,1,3
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_two(starting_numbers, 30000000)
    assert result == 3544142

def test_solve_two_4():
    input = """
    1,2,3
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_two(starting_numbers, 30000000)
    assert result == 261214

def test_solve_two_6():
    input = """
    2,3,1
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_two(starting_numbers, 30000000)
    assert result == 6895259

def test_solve_two_7():
    input = """
    3,2,1
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_two(starting_numbers, 30000000)
    assert result == 18

def test_solve_two_8():
    input = """
    3,1,2
    """.strip().replace('    ', '')
    starting_numbers = parse_input(input)
    result = solve_two(starting_numbers, 30000000)
    assert result == 362