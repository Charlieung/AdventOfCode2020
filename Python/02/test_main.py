import pytest
from main import solve_one, solve_two

@pytest.fixture
def password_policies():
    return [
        (1, 3, 'a', 'abcde'),
        (1, 3, 'b', 'cdefg'),
        (2, 9, 'c', 'ccccccccc')
        ]

def test_solve_one(password_policies):
    valid_passwords = solve_one(password_policies)
    assert valid_passwords == 2

def test_solve_two(password_policies):
    valid_passwords = solve_two(password_policies)
    assert valid_passwords == 1