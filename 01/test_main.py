import pytest
from main import solve_one

@pytest.fixture
def expense_report():
    return [1721, 979, 366, 299, 675, 1456]

def test_solve_one(expense_report):
    product = solve_one(expense_report, 2020)
    assert product == 514579
