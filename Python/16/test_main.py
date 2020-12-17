from attr import Factory
import pytest

from main import parse_input, solve_one, solve_two
from ticket import TicketFactory

@pytest.fixture
def ticket_details_one():
    input = """
    class: 1-3 or 5-7
    row: 6-11 or 33-44
    seat: 13-40 or 45-50

    your ticket:
    7,1,14

    nearby tickets:
    7,3,47
    40,4,50
    55,2,20
    38,6,12
    """.strip().replace('    ', '')
    requirements, personal_ticket, other_tickets = parse_input(input)
    return requirements, personal_ticket, other_tickets

@pytest.fixture
def ticket_details_two():
    input = """
    class: 0-1 or 4-19
    row: 0-5 or 8-19
    seat: 0-13 or 16-19

    your ticket:
    11,12,13

    nearby tickets:
    3,9,18
    15,1,5
    5,14,9
    """.strip().replace('    ', '')
    requirements, personal_ticket, other_tickets = parse_input(input)
    return requirements, personal_ticket, other_tickets

def test_solve_one(ticket_details_one):
    requirements, personal_ticket, other_tickets = ticket_details_one
    factory = TicketFactory(requirements)
    result = solve_one(factory, other_tickets)
    assert result == 71

def test_solve_two(ticket_details_two):
    requirements, personal_ticket, other_tickets = ticket_details_two
    factory = TicketFactory(requirements)
    result = solve_two(factory, other_tickets, personal_ticket)
    assert result.ROW == 11
    assert result.CLASS == 12
    assert result.SEAT == 13