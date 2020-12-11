import os, logging
import numpy as np

from datetime import datetime as dt

from numpy.core.einsumfunc import _parse_possible_contraction
from functools import lru_cache

from numpy.lib.function_base import diff

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def timeit(f):
    def wrap(*args, **kwargs):
        start_time = dt.now()
        result = f(*args, **kwargs)
        if result:
            end_time = dt.now()
            logging.info(f'Time Elapsed: {end_time - start_time}')
        return result
    return wrap                            

def parse_input(input):
    adapters = [int(line) for line in input.split('\n')]
    return adapters


@timeit
def solve_one(adapters):
    adapters.sort()
    rating = max(adapters) + 3
    adapters = [0] + adapters + [rating]
    differences = np.diff(adapters).tolist()
    number = differences.count(3) * differences.count(1)
    logging.info(f'Number: {number}')
    return number

@timeit
def solve_two(adapters):
    adapters.sort()
    rating = max(adapters) + 3
    adapters = [0] + adapters + [rating]
    differences = np.diff(adapters).tolist()

    @lru_cache
    def search(index=0):
        if index == len(differences) - 1:
            return 1
        else:
            relative_difference = differences[index:]
            total_difference = np.cumsum(relative_difference)
            possibilities = len([d for d in total_difference if d < 4])
            indicies = index + 1 + np.arange(possibilities) # possible consecutive indicies
            return sum([search(i) for i in indicies])

    arrangements = search()
    logging.info(f'Arrangements: {arrangements}')
    return arrangements

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        adapters = parse_input(f.read().strip())

    # part 1
    logging.info('[Part 1]')
    solve_one(adapters)

    # part 2
    logging.info('[Part 2]')
    solve_two(adapters) 