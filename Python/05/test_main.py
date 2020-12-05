import pytest
#from main import solve_one
from seat import Seat

@pytest.fixture
def boarding_passes():
    return [
        'FBFBBFFRLR',
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL'
    ]

def test_seat(boarding_passes):
    properties = [
        (44, 5, 357),
        (70, 7, 567),
        (14, 7, 119),
        (102, 4, 820),
    ]
    tests = zip(boarding_passes, properties)
    for code, props in tests:
        row, column, id = props
        seat = Seat(code)
        assert seat.row == row
        assert seat.column == column
        assert seat.id == id
