import os, logging
import itertools

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
    transmission = [int(line) for line in input.split('\n')]
    return transmission


@timeit
def solve_one(transmission, window):
    preamble = transmission[:window]
    feed = transmission[window:]

    for number in feed:
        possibilities = [option for option in preamble if option < number]
        sums = [sum(pair) for pair in itertools.combinations(possibilities, 2)]
        if number in sums:
            preamble.pop(0)
            preamble.append(number)
        else:
            break
    logging.info(f'Number: {number}')
    return number

@timeit
def solve_two(transmission, number):
    possibilities = [option for option in transmission if option < number]
    print(possibilities)
    combinations = itertools.chain(*map(lambda x: itertools.combinations(possibilities, x), range(0, len(possibilities)+1)))
    for combo in combinations:
        if sum(combo) == number:
            break
    weakness = min(combo) + max(combo)
    logging.info(f'Weakness: {weakness}')
    return weakness

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        transmission = parse_input(f.read().strip())

    # part 1
    logging.info('[Part 1]')
    window = 25
    solve_one(transmission, window)

    # part 2
    logging.info('[Part 2]')
    solve_two(transmission, number) 