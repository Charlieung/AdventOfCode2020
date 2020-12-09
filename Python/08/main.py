import os, logging
from datetime import datetime as dt

from console import Console
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
def solve_one(boot_code):
    console = Console(boot_code)    
    console.boot()
    logging.info(f'Accumulator: {console.accumulator}')
    return console.accumulator

@timeit
def solve_two(boot_code):
    console = Console(boot_code)

    # identify jmp indices
    jmps, nops = [], []
    
    i = 0
    while i < len(console.boot_code):
        instruction = console.boot_code[i]
        if instruction.operation == 'jmp':
            jmps.append(i)
        elif instruction.operation == 'nop':
            nops.append(i)
        i+= 1

    # brute force replace
    for i in (jmps + nops):
        instruction = console.boot_code[i]
        instruction.operation = 'nop 'if i in jmps else 'jmp'
        console.boot_code[i] = instruction

        if console.boot():
            logging.info(f'Accumulator: {console.accumulator}')
            return console.accumulator
        else:
            # reset console
            console.reset()
    return

if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        boot_code = f.read().strip()

    # part 1
    logging.info('[Part 1]')
    solve_one(boot_code)

    # part 2
    logging.info('[Part 2]')
    solve_two(boot_code)