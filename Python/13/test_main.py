import pytest

from main import parse_input, solve_one, solve_two

@pytest.fixture
def travel_plan():
    input = """
    939
    7,13,x,x,59,x,31,19
    """.strip().replace('    ', '')
    travel_plan = parse_input(input)
    return travel_plan

def test_solve_one(travel_plan):
    departure_time, schedules = travel_plan
    assert solve_one(departure_time, schedules) == 295

def test_solve_two(travel_plan):
    departure_time, schedules = travel_plan
    assert solve_two(schedules) == 1068781

def test_solve_two_alt_one():
    schedules = parse_input("""
    0
    17,x,13,19
    """.strip().replace('    ', ''))[1]
    assert solve_two(schedules) == 3417

def test_solve_two_alt_two():
    schedules = parse_input("""
    0
    67,7,59,61
    """.strip().replace('    ', ''))[1]
    assert solve_two(schedules) == 754018

def test_solve_two_alt_three():
    schedules = parse_input("""
    0
    67,x,7,59,61
    """.strip().replace('    ', ''))[1]
    assert solve_two(schedules) == 779210

def test_solve_two_alt_four():
    schedules = parse_input("""
    0
    67,7,x,59,61
    """.strip().replace('    ', ''))[1]
    assert solve_two(schedules) == 1261476

def test_solve_two_alt_five():
    schedules = parse_input("""
    0
    1789,37,47,1889
    """.strip().replace('    ', ''))[1]
    assert solve_two(schedules) == 1202161486