import os, logging
import numpy as np
from datetime import datetime as dt

from seat import Seat
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
def solve_one(boarding_passes):
    highest_seat_id = 0
    for boarding_pass in boarding_passes:
        seat = Seat(boarding_pass)
        highest_seat_id = max(seat.id, highest_seat_id)

    logging.info(f'Highest Seat ID: {highest_seat_id}')
    return highest_seat_id

@timeit
def solve_two(boarding_passes):
    seat_map = np.zeros((128, 8))
    for boarding_pass in boarding_passes:
        seat = Seat(boarding_pass)
        seat_map[seat.row, seat.column] = seat.id

    neighbors = seat_map.flatten()
    neighbors = np.where(neighbors > 0)
    seat_id = np.sum(range(np.min(neighbors), np.max(neighbors) + 1)) - np.sum(neighbors)
    logging.info(f'Seat ID: {seat_id}')
    return seat_id

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        boarding_passes = f.read().strip().split('\n')

    # part 1
    logging.info('[Part 1]')
    solve_one(boarding_passes)

    # part 2
    logging.info('[Part 2]')
    solve_two(boarding_passes)