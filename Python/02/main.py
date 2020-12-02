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

@timeit
def solve_one(password_policies):
    valid_passwords = 0
    for password_policy in password_policies:
        min, max, letter, password = password_policy
        letter_count = password.count(letter)
        if min <= letter_count <= max:
            valid_passwords += 1
    logging.info(f'Valid Passwords: {valid_passwords}')
    return valid_passwords

@timeit
def solve_two(password_policies):
    valid_passwords = 0
    for password_policy in password_policies:
        min, max, letter, password = password_policy
        if (password[min - 1] == letter) ^ (password[max - 1] == letter):
            valid_passwords += 1
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