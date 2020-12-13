import os, logging
import numpy as np

from datetime import datetime as dt
from ship import Ship, Waypoint


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
    # Parse instructions into 
    # direction, magnitude later in case part 2 changes
    instructions = [(line[0], int(line[1:])) for line in input.split('\n')]
    return instructions


@timeit
def solve_one(instructions):
    ship = Ship()
    for instruction in instructions:
        ship.move(instruction)
    manhattan_distance = sum(np.abs(ship.position))
    logging.info(f'Manhattan Distance: {manhattan_distance}')
    return manhattan_distance

@timeit
def solve_two(instructions):
    ship = Ship()
    waypoint = Waypoint()
    for instruction in instructions:
        if instruction[0] == 'F':
            waypoint.transport(ship, instruction[1])
        else:
            waypoint.move(instruction)
    manhattan_distance = sum(np.abs(ship.position))
    logging.info(f'Manhattan Distance: {manhattan_distance}')
    return manhattan_distance

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