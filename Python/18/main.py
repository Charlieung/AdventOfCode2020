import os, logging, numpy as np
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

def solve_equation_one(input):
    input = input.replace(' ', '')
    
    numbers = []
    operations = []
    
    i = 0
    while i < len(input):
        char = input[i]
        if char in ['+', '*']:
            operations.append(char)
        elif char == '(':
            parenthesis_count = 1
            subequation = ''
            while parenthesis_count != 0:
                subequation += char
                i += 1
                char = input[i]
                if char == '(':
                    parenthesis_count += 1
                if char == ')':
                    parenthesis_count -= 1
            subequation = subequation[1:] # remove initial '('
            subanswer = solve_equation_one(subequation)
            numbers.append(subanswer)
        else:
            numbers.append(int(char))
        i += 1
    
    answer = numbers.pop(0)
    for number, operation in zip(numbers, operations):
        if operation == '*':
            answer *= number
        elif operation == '+':
            answer += number
        else:
            raise ValueError(f'Invalid Operation: {operation}')
    return answer

def solve_equation_two(input):
    input = input.replace(' ', '')
    
    numbers = []
    operations = []
    
    i = 0
    while i < len(input):
        char = input[i]
        if char in ['+', '*']:
            operations.append(char)
        elif char == '(':
            parenthesis_count = 1
            subequation = ''
            while parenthesis_count != 0:
                subequation += char
                i += 1
                char = input[i]
                if char == '(':
                    parenthesis_count += 1
                if char == ')':
                    parenthesis_count -= 1
            subequation = subequation[1:] # remove initial '('
            subanswer = solve_equation_two(subequation)
            numbers.append(subanswer)
            if operations and operations[-1] == '+':
                number_one = numbers.pop()
                number_two = numbers.pop()
                operations.pop()
                numbers.append(number_one + number_two)
        else:
            numbers.append(int(char))
            if operations and operations[-1] == '+':
                number_one = numbers.pop()
                number_two = numbers.pop()
                operations.pop()
                numbers.append(number_one + number_two)
        i += 1

        answer = np.prod(np.array(numbers, dtype=np.int64))
    return answer


@timeit
def solve_one(input):
    answer = 0
    for line in input.split('\n'):
        answer += solve_equation_one(line)
    logging.info(f'answer = {answer}')
    return answer

@timeit
def solve_two(input):
    answers = np.array([], dtype=np.int64)
    for line in input.split('\n'):
        answers = np.append(answers, solve_equation_two(line))
    
    answer = np.sum(answers)

    logging.info(f'answer = {answer}')
    return answer


if __name__ == '__main__':
    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        input = f.read().strip()

    # part 1
    logging.info('[Part 1]')
    solve_one(input)

    # # part 2
    logging.info('[Part 2]')
    solve_two(input)