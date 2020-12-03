import os, logging
import numpy as np
from datetime import datetime as dt

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
def solve_one(geology, slope):
    rows = geology.split('\n')
    geology = np.array(rows) \
        .view('<U1') \
        .reshape(len(rows), -1) \
        == '#'
    
    x, y = slope
    height, width = geology.shape
    run_width = int(np.ceil(- height / y * x))
    if width < run_width:
        factor = int(np.ceil(run_width / width))
        geology = np.tile(geology, (1, factor))
        width = geology.shape[1]
    
    mask = np.mod(np.arange(width * height).reshape(height, width), width * - y + x) == 0
    trees = np.sum(np.logical_and(mask, geology))
    logging.info(f'Trees: {trees}')
    return trees

@timeit
def solve_two(geology, slopes):
    product = 1
    for slope in slopes:
        logging.info(f'Slope: {slope}')
        product *= int(solve_one(geology, slope))
    logging.info(f'Product: {product}')
    return product

if __name__ == '__main__':
    ## setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        geology = f.read().strip()
    
    # part 1
    logging.info('[Part 1]')
    solve_one(geology, (3, -1))

    # part 2
    logging.info('[Part 2]')
    slopes = [
        (1, -1),
        (3, -1),
        (5, -1),
        (7, -1),
        (1, -2),
        ]
    solve_two(geology, slopes)