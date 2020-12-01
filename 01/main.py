import os, logging
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
def solve_one(expense_report, total):
    
    inverse = set([total - x for x in expense_report])
    try:
        a, b = inverse.intersection(expense_report)
    except:
        return None
    product = a * b
    logging.info(f'{a} * {b} = {product}')
    return product

@timeit
def solve_two(expense_report, total):
    for x in expense_report:
        new_total = total - x
        product = solve_one(expense_report, new_total)
        if not product:
            continue
        else:
            logging.info(f'{x} * {product} = {x * product}')
            return x * product

if __name__ == '__main__':
    # setup
    current_directory = os.path.dirname(__file__)
    with open(f'{current_directory}/input.txt') as f:
        input = f.read().strip()
    expense_report = [int(x) for x in input.split('\n')]    

    # part 1
    logging.info('[Part 1]')
    solve_one(expense_report, 2020)

    # part 2
    logging.info('[Part 2]')
    solve_two(expense_report, 2020)