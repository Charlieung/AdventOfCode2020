import os, logging
import numpy as np

from datetime import datetime as dt
from functools import lru_cache
from itertools import permutations


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
    seat_layout = np.matrix(input\
        .replace('\n', ';') \
        .replace('L', '-1 ') \
        .replace('.', '0 '))
    return seat_layout


@timeit
def solve_one(seat_layout):
    
    def count_neighbors(i, j, matrix):
        height, width = matrix.shape
        generate_bounds = lambda x, size: (max(0, x - 1), min(size, x + 1) + 1)
        current_seat_is_taken = matrix[i, j] == 1
        lbound_x, ubound_x = generate_bounds(j, width)
        lbound_y, ubound_y = generate_bounds(i, height)
        neighbor_layout = matrix[lbound_y: ubound_y, lbound_x: ubound_x]
        neighbor_seats = np.equal(neighbor_layout, 1)
        neighbors = np.sum(neighbor_seats) - current_seat_is_taken
        return neighbors
    
    def predict_one_round(current_state):
        future_state = current_state.copy()
        height, width = current_state.shape
        for i in range(height):
            for j in range(width):
                # Rule: if seat is empty, and if all around you is empty
                is_empty_seat = current_state[i, j] == -1
                is_taken_seat = current_state[i, j] == 1
                is_empty_floor = current_state[i, j] == 0
                if not is_empty_floor:
                    neighbors = count_neighbors(i, j, current_state)
                    if is_empty_seat:
                        seat_has_no_neighbors = neighbors == 0
                        if seat_has_no_neighbors:
                            future_state[i, j] = 1 # take seat
                    elif is_taken_seat:
                        seat_has_too_many_neighbors = neighbors >= 4
                        if seat_has_too_many_neighbors:
                            future_state[i, j] = -1 # leave seat
        return future_state

    future_state = seat_layout
    stable = False
    while not stable:
        current_state = future_state
        future_state = predict_one_round(current_state)
        stable = (current_state == future_state).all()
        
    occupied_seats = np.sum(np.equal(future_state, 1))
    logging.info(f'Occupied Seats: {occupied_seats}')
    return occupied_seats

@timeit
def solve_two(seat_layout):
    def predict_one_round(current_state):
        future_state = current_state.copy()
        height, width = current_state.shape

        # current state matrix is necessary global for lru cache
        # vector is (vx, vy) format
        @lru_cache
        def find_neighbor(i, j, vx, vy):
            try:
                if i + vy < 0 or j + vx < 0:
                    raise IndexError()
                next_position = current_state[i + vy, j + vx] 
            except IndexError:
                return 0
            # print(f'({j + vx}, {i + vy}): {next_position}')
            if next_position == 0:
                return find_neighbor(i + vy, j + vx, vx, vy)
            else:
                return max(next_position, 0)

        def count_neighbors(i, j):
            vectors = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, 1),
                (-1, -1),
                (1, -1),
                (-1, 1),
            ]
            neighbors = 0
            for vector in vectors:
                vx, vy = vector
                neighbors += find_neighbor(i, j, vx, vy)

            return neighbors
        

        for i in range(height):
            for j in range(width):
                # Rule: if seat is empty, and if all around you is empty
                is_empty_seat = current_state[i, j] == -1
                is_taken_seat = current_state[i, j] == 1
                is_empty_floor = current_state[i, j] == 0
                if not is_empty_floor:
                    neighbors = count_neighbors(i, j)
                    if is_empty_seat:
                        seat_has_no_neighbors = neighbors == 0
                        if seat_has_no_neighbors:
                            future_state[i, j] = 1 # take seat
                    elif is_taken_seat:
                        seat_has_too_many_neighbors = neighbors >= 5
                        if seat_has_too_many_neighbors:
                            future_state[i, j] = -1 # leave seat
        return future_state

    future_state = seat_layout
    stable = False
    while not stable:
        current_state = future_state
        future_state = predict_one_round(current_state)
        stable = (current_state == future_state).all()
        
    occupied_seats = np.sum(np.equal(future_state, 1))
    logging.info(f'Occupied Seats: {occupied_seats}')
    return occupied_seats

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        seat_layout = parse_input(f.read().strip())

    # part 1
    logging.info('[Part 1]')
    solve_one(seat_layout)

    # part 2
    logging.info('[Part 2]')
    solve_two(seat_layout) 