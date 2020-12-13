import os, logging
import numpy as np

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
    departure_time, schedules = input.split('\n')
    departure_time = int(departure_time)
    schedules = np.array([int(schedule) if schedule != 'x' else np.nan for schedule in schedules.split(',')])
    return departure_time, schedules


@timeit
def solve_one(departure_time, schedules):
    schedules = schedules[~np.isnan(schedules)] # Remove Null
    earliest_availabilities = schedules * np.ceil(departure_time / schedules)
    earliest_availability = np.min(earliest_availabilities)
    where_min = np.where(earliest_availabilities == earliest_availability)[0]
    best_schedule = int(schedules[where_min][0])
    wait_time = int(earliest_availability - departure_time)
    product = best_schedule * wait_time
    logging.info(f'Best Schedule ({best_schedule}) * Wait Time ({wait_time}) = {product}')
    return product

@timeit
def solve_two_brute_force(schedules):
    schedules = np.where(np.isnan(schedules), 1, schedules)
    schedules = schedules[~np.isnan(schedules)] # Remove Null
    offsets = np.arange(len(schedules))
    synchronized = np.array([False])
    
    # Increment by largest schedule to save time
    increment = np.max(schedules)
    position = int(np.where(schedules==increment)[0])
    earliest_offsetting_timestamp = 0 # use initial as start
    while not synchronized.all():
        earliest_offsetting_timestamp += increment
        departures = offsets + earliest_offsetting_timestamp - position
        synchronized = np.mod(departures, schedules) == 0
    earliest_offsetting_timestamp -= position
    logging.info(f'Earliest Offsetting Timestamp: {int(earliest_offsetting_timestamp)}')
    return earliest_offsetting_timestamp

@timeit
def solve_two(schedules):
    # Implementation of Chinese Remainder Theorem
    where_has_schedule = ~np.isnan(schedules)
    remainders = np.arange(len(schedules))[where_has_schedule]
    schedules = schedules[where_has_schedule]
    remainders = schedules - remainders # solving for one side makes remainders negative

    # System of congruence is then solving for quotient modulo schedules
    product = reduce(lambda x, y: int(x) * int(y), schedules)
    subproducts = product / schedules

    def invert(number, modulo):
        number = number % modulo
        for i in range(int(modulo)):
            if (number * i) % modulo == 1:
                return i

    inverses = [invert(subproduct, schedule) for subproduct, schedule in zip(subproducts, schedules)]
    result = sum([int(remainder) * int(subproduct) * int(inverse) for (remainder, subproduct, inverse) in zip(remainders, subproducts, inverses)])
    earliest_offsetting_timestamp = result % product
    logging.info(f'Earliest Offsetting Timestamp: {earliest_offsetting_timestamp}')
    return earliest_offsetting_timestamp

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        departure_time, schedules = parse_input(f.read().strip())

    # part 1
    logging.info('[Part 1]')
    solve_one(departure_time, schedules)

    # part 2
    logging.info('[Part 2]')
    solve_two(schedules) 