from dataclasses import dataclass

@dataclass
class Instruction:
    operation: str
    value: int
    visits: int = 0
    
class Console:
    def __init__(self, input):
        self.__input = input
        self.boot_code = Console.parse_input(input)
        self.accumulator = 0
        self.index = 0
    
    @staticmethod
    def parse_input(input):
        lines = input.split('\n')
        instructions = []
        for line in lines:
            operation, value = line.strip().split(' ')
            value = int(value)
            instruction = Instruction(operation, value)
            instructions.append(instruction)
        return instructions

    def boot(self):
        while self.index < len(self.boot_code):
            instruction = self.boot_code[self.index]
            instruction.visits += 1
            if instruction.visits > 1:
                return False
            else:
                if instruction.operation == 'acc':
                    self.accumulator += instruction.value
                    self.index += 1
                elif instruction.operation == 'jmp':
                    self.index += instruction.value
                else:
                    self.index += 1
        return True
    
    def reset(self):
        self.index = 0
        self.accumulator = 0
        self.boot_code = Console.parse_input(self.__input)
        