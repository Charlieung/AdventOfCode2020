import os, logging
import numpy as np

from datetime import datetime as dt

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
    starting_numbers = [int(number) for number in input.split(',')]
    return starting_numbers

@timeit
def solve_one(starting_numbers, index):
    # init values
    memory = {k: v for (v, k) in zip(range(len(starting_numbers)), starting_numbers)}
    start = len(starting_numbers)
    last_insertion = None # flag to keep track if last number was new
    # iterate and keep track of unique indices
    for i in range(start, index):
        if last_insertion is None:
            spoken_number = 0
        else:
            spoken_number = i - last_insertion - 1
        last_insertion = memory.get(spoken_number)
        memory[spoken_number] = i
    number = spoken_number
    logging.info(f'{index}th Number: {number}')
    return number

def solve_two(starting_numbers, index):
    number = solve_one(starting_numbers, index)
    return number


if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        starting_numbers = parse_input(f.read().strip())

    # part 1
    logging.info('[Part 1]')
    solve_one(starting_numbers, 2020)

    # part 2
    logging.info('[Part 2]')
    solve_two(starting_numbers, 30000000)


