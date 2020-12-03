import pytest
from main import solve_one, solve_two

@pytest.fixture
def geology():
    return """
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    """.strip().replace('    ', '')

def test_solve_one(geology):
    trees = solve_one(geology, (3, -1))
    assert trees == 7

def test_solve_two(geology):
    slopes = [
        (1, -1),
        (3, -1),
        (5, -1),
        (7, -1),
        (1, -2),
        ]
    product = solve_two(geology, slopes)
    assert product == 336