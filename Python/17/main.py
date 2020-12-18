import os, logging
import numpy as np

from datetime import datetime as dt
from grid import Grid

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def timeit(f):
    def wrap(*args, **kwargs):
        start_time = dt.now()
        result = f(*args, **kwargs)
        if result is not None:
            end_time = dt.now()
            logging.info(f'Time Elapsed: {end_time - start_time}')
        return result
    return wrap                            

def parse_input(input):
    """Active State: 1, Inactivate State: 0"""
    state = np.matrix(input \
        .replace('.', '0 ') \
        .replace('#', '1 ') \
        .replace('\n', ';'))
    return state

@timeit
def solve_one(initial_state, cycles):
    grid = Grid(initial_state)
    print(grid)
    for _ in range(cycles):
        grid.cycle()

    answer = grid.count_active_cubes()
    logging.info(f'Answer = {answer}')
    return answer

@timeit
def solve_two(initial_state, cycles):
    answer = 0
    logging.info(f'Answer = {answer}')
    return answer


if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        initial_state = parse_input(f.read().strip())
    
    # part 1
    logging.info('[Part 1]')
    solve_one(initial_state, 6)

    # part 2
    logging.info('[Part 2]')
    solve_two(initial_state, 6)


