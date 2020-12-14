import os, logging
import numpy as np

from decoder import Decoder, UpdatedDecoder
from datetime import datetime as dt
from functools import reduce

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
    instructions = input.split('\n')
    return instructions

@timeit
def solve_one(instructions):
    decoder = Decoder()
    decoder.feed(instructions)
    complete_sum = sum(decoder.memory.values())
    logging.info(f'Complete Sum = {complete_sum}')
    return complete_sum

@timeit
def solve_two(instructions):
    decoder = UpdatedDecoder()
    decoder.feed(instructions)
    complete_sum = sum(decoder.memory.values())
    logging.info(f'Complete Sum = {complete_sum}')
    return complete_sum


if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        instructions = parse_input(f.read().strip())

    # part 1
    logging.info('[Part 1]')
    solve_one(instructions)

    # part 2
    logging.info('[Part 2]')
    solve_two(instructions)


