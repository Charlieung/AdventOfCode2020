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

def parse_input(input):
    seat_layout = np.loadtxt(input)
    return seat_layout


@timeit
def solve_one(seat_layout):
    final_state = seat_layout
    return final_state

@timeit
def solve_two(seat_layout):
    final_state = seat_layout
    return final_state

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        seat_layout = parse_input(f.read().strip())

    print(seat_layout)
    # part 1
    logging.info('[Part 1]')
    solve_one(seat_layout)

    # part 2
    logging.info('[Part 2]')
    solve_two(seat_layout) 