import os, logging
from datetime import datetime as dt

from passport import Passport
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
def solve_one(passports):
    valid_passports = 0
    for passport in passports:
        try:
            Passport(**passport)
            valid_passports += 1
        except:
            pass

    logging.info(f'Valid Passports: {valid_passports}')
    return valid_passports

@timeit
def solve_two(passports):
    valid_passports = 0
    for passport in passports:
        try:
            passport = Passport(**passport)
            if passport.is_valid():
                valid_passports += 1
        except:
            pass

    logging.info(f'Valid Passports: {valid_passports}')
    return valid_passports

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        passport_text = f.read().strip()
    records = passport_text.split('\n\n')
    records = [record.replace('\n', ' ').split(' ') for record in records]
    passports = []
    for record in records:
        passport = {}
        for entry in record:
            key, value = entry.split(':')
            passport[key] = value
        passports.append(passport)

    # part 1
    logging.info('[Part 1]')
    solve_one(passports)

    # part 2
    logging.info('[Part 2]')
    solve_two(passports)