# import numba
import struct
import numpy as np

from itertools import permutations
from collections import namedtuple

class TicketFactory:
    def __init__(self, requirements):
        self.requirements = TicketFactory.parse_requirements(requirements.split('\n'))
        self.structure = None

    @staticmethod
    def parse_requirements(lines):
        fields = {}
        for line in lines:
            field, valid_values = line.split(': ')
            first_values, second_values = valid_values.split(' or ')
            first_lbound, first_ubound = first_values.split('-')
            second_lbound, second_ubound = second_values.split('-')
            first_lbound, first_ubound, second_lbound, second_ubound = \
                int(first_lbound), int(first_ubound), int(second_lbound), int(second_ubound)
            fields[TicketFactory.string_normalize(field)] = \
                first_lbound, first_ubound, second_lbound, second_ubound
        return fields

    @staticmethod
    def string_normalize(text):
        text = text.upper().replace(' ', '_')
        return text

    def define_structure(self, tickets):
        fields = list(self.requirements.keys())
        rows, columns = tickets.shape
        boolean_array = np.ones(rows) # per row
        possibilities = {field: [] for field in fields}
        # There must be a column with only one possibility or else the system is cyclic and there is no unique solution
        for i in range(columns):
            values = np.hstack(tickets[:, i])
            for j in range(columns):
                field = fields[j]
                bounds = self.requirements.get(field)
                first_lbound, first_ubound, second_lbound, second_ubound = bounds
                boolean_array = np.logical_or(
                        np.logical_and(first_lbound <= values, values <= first_ubound),
                        np.logical_and(second_lbound <= values, values <= second_ubound),
                    )

                # Attach possilbiilty
                if boolean_array.all():
                    possibilities[field].append(i)
        
        solve_order = list(possibilities.keys())
        solve_order.sort(key=lambda x: len(possibilities[x]))
        
        solution = {}
        while possibilities:
            for field in solve_order:
                if field not in possibilities:
                    continue
                if len(possibilities[field]) == 1:
                    index = possibilities[field][0]
                    solution[field] = index
                    possibilities.pop(field)
                    # remove this index from all other columns as its' claimed
                    for field in possibilities:
                        if index in possibilities[field]:
                            possibilities[field].remove(index)
                else:
                    continue

        structure = list(solution.keys())
        structure.sort(key=lambda x: solution[x])
        self.structure = namedtuple('Ticket', structure)

    def check_values(self, tickets):
        boolean_matrix = np.zeros(tickets.shape)
        for bounds in self.requirements.values():
            first_lbound, first_ubound, second_lbound, second_ubound = bounds
            boolean_matrix = np.logical_or(
                boolean_matrix, 
                np.logical_or(
                    np.logical_and(first_lbound <= tickets, tickets <= first_ubound),
                    np.logical_and(second_lbound <= tickets, tickets <= second_ubound),
                )
            )
        
        invalid_fields = np.where(~boolean_matrix, tickets, np.nan)
        return invalid_fields


    def generate_ticket(self, *args, **kwargs):
        ticket = self.structure(*args, **kwargs)
        return ticket

