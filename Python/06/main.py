import os, logging

from datetime import datetime as dt
from functools import reduce

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

@timeit
def solve_one(declaration_forms):
    groups = declaration_forms.split('\n\n')
    yes_counts = sum([len(set(group.replace('\n', ''))) for group in groups])
    logging.info(f'Yes Counts: {yes_counts}')
    return yes_counts

@timeit
def solve_two(declaration_forms):
    groups = declaration_forms.split('\n\n')
    yes_counts = sum([len((reduce(lambda x, y: set(x) & set(y), group.split('\n')))) for group in groups])
    logging.info(f'Yes Counts: {yes_counts}')
    return yes_counts

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        declaration_forms = f.read().strip()

    # part 1
    logging.info('[Part 1]')
    solve_one(declaration_forms)

    # part 2
    logging.info('[Part 2]')
    solve_two(declaration_forms)