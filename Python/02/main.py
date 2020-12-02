import os, logging
import numpy as np
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
def solve_one(password_policies):
    
    broadcast = lambda x: np.repeat(x, 20).reshape((password_count, 20))

    password_policies = np.array(
        password_policies, 
        dtype=np.dtype([
            ('first', np.int64),
            ('second', np.int64),
            ('letter', '<U1'),
            ('password', 'U20'),
        ])
    )

    password_count = len(password_policies)
    first = password_policies['first']
    second = password_policies['second']
    letter = password_policies['letter']
    password = password_policies['password']
    password = np.char.ljust(password, 20)\
        .view('<U1')\
        .reshape((password_count, -1))

    broadcast = lambda x: np.repeat(x, 20).reshape((password_count, 20))
    matches = np.char.equal(password, broadcast(letter))
    match_counts = np.sum(matches, axis=1)

    valid_passwords = np.sum(np.logical_and(
        match_counts >= first, 
        match_counts <= second, 
    ))
    logging.info(f'Valid Passwords: {valid_passwords}')
    return valid_passwords

@timeit
def solve_two(password_policies):

    broadcast = lambda x: np.repeat(x, 20).reshape((password_count, 20))

    password_policies = np.array(
        password_policies, 
        dtype=np.dtype([
            ('first', np.int64),
            ('second', np.int64),
            ('letter', '<U1'),
            ('password', 'U20'),
        ])
    )

    password_count = len(password_policies)
    first = password_policies['first']
    second = password_policies['second']
    letter = password_policies['letter']
    password = password_policies['password']
    password = np.char.ljust(password, 20)\
        .view('<U1')\
        .reshape((password_count, -1))

    matches = np.char.equal(password, broadcast(letter))

    indexer = np.arange(20) \
        .repeat(password_count) \
        .reshape(20, password_count) \
        .transpose() + 1

    mask = np.logical_or(
        indexer == broadcast(first), 
        indexer == broadcast(second)
    )

    valid_passwords = np.sum(np.sum(
        np.logical_and(matches, mask), 
        axis=1) == 1)

    logging.info(f'Valid Passwords: {valid_passwords}')
    return valid_passwords

if __name__ == '__main__':
    # setup
    current_directory = os.path.dirname(__file__)
    with open(f'{current_directory}/input.txt') as f:
        lines = f.read().strip().split('\n')
    password_policies = []
    print(len(lines))
    for line in lines:
        policy, password = line.split(': ', 1)
        bounds, letter = policy.split(' ', 1)
        min, max = bounds.split('-')
        min, max = int(min), int(max)
        entry = min, max, letter, password
        password_policies.append(entry)

    # part 1
    logging.info('[Part 1]')
    solve_one(password_policies)

    # part 2
    logging.info('[Part 2]')
    solve_two(password_policies)