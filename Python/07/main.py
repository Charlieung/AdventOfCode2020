import os, logging
from datetime import datetime as dt

from bag import Bag, BagFactory
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
def solve_one(rules, color):
    factory = BagFactory(rules)
    count = 0
    for key in factory.rules.keys():
        if key == color: # ignore instance where directly using color
            continue
        else:
            bag = factory.generate_bag(key)
            if bag.find(color):
                count += 1
    logging.info(f'Count: {count}')
    return count

@timeit
def solve_two(rules, color):
    factory = BagFactory(rules)
    bag = factory.generate_bag(color)
    count = bag.count() - 1 # exclude initial bag
    logging.info(f'Count: {count}')
    return count

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        rules = f.read().strip()

    color = 'shiny gold'

    # part 1
    logging.info('[Part 1]')
    solve_one(rules, color)

    # part 2
    logging.info('[Part 2]')
    solve_two(rules, color)