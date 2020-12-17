import os, logging
import numpy as np

from datetime import datetime as dt
from ticket import TicketFactory

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
    requirements, personal_ticket, other_tickets = input.split('\n\n')
    parse_ticket = lambda x: [int(value) for value in x.split(',')]
    personal_ticket = parse_ticket(personal_ticket.split('\n')[1])
    other_tickets = np.matrix(';'.join(other_tickets.split('\n')[1:]))
    return requirements, personal_ticket, other_tickets

@timeit
def solve_one(factory, tickets):
    invalid_fields = factory.check_values(tickets)
    where_valid = ~np.isnan(invalid_fields)
    error_rate = np.sum(invalid_fields[where_valid])
    logging.info(f'Error Rate = {error_rate}')
    return error_rate

@timeit
def solve_two(factory, tickets, personal_ticket):
    invalid_fields = factory.check_values(tickets)
    where_valid = np.isnan(invalid_fields).all(axis=1)
    valid_tickets = tickets[where_valid]
    factory.define_structure(valid_tickets)
    ticket = factory.generate_ticket(*personal_ticket)
    logging.info(f'Ticket = {ticket}')
    # Answer
    product = 1
    for key, value in ticket._asdict().items():
        if key.startswith('DEPARTURE'):
            product *= value
    logging.info(f'Departure Product = {product}')
    return ticket


if __name__ == '__main__':

    # setup
    current_directory = os.path.dirname(__file__) or os.curdir
    with open(f'{current_directory}/input.txt') as f:
        requirements, personal_ticket, other_tickets = parse_input(f.read().strip())

    # print(other_tickets[116, 19]) # 0 value
    factory = TicketFactory(requirements)
    
    # part 1
    logging.info('[Part 1]')
    solve_one(factory, other_tickets)

    # part 2
    logging.info('[Part 2]')
    solve_two(factory, other_tickets, personal_ticket)


