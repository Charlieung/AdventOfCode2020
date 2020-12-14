from itertools import product

class Decoder:
    def __init__(self):
        self.memory = {}
        self.transform = None
    
    def update_transform(self, line):
        """
        nullmask defines what to keep from the original value: 1's for keeping, 0's for removing
        writemask is a representation of what gets written. 0 is everything that's not being written
        """
        bitmask = line.replace('mask = ', '')
        nullmask = int('0b' + bitmask.replace('1', '0').replace('X', '1'), 2)
        writemask = int('0b' + bitmask.replace('X', '0'), 2)
        transform = lambda value: value & nullmask | writemask
        self.transform = transform
    
    def update_memory(self, line):
        address, value = line \
            .replace('mem[', '') \
            .replace(']', '') \
            .split(' = ', 1)
        address = int(address)
        value = int(value)
        self.memory[address] = self.transform(value)
    
    def update(self, line):
        if line.startswith('mask'):
            self.update_transform(line)
        else:
            self.update_memory(line)
    
    def feed(self, instructions):
        for line in instructions:
            self.update(line)

class UpdatedDecoder(Decoder):
    def update_transform(self, line):
        bitmask = line.replace('mask = ', '')
        nullmask = int('0b' + bitmask.replace('0', '1').replace('X', '0'), 2)
        floats = bitmask.count('X')

        def transform(value):
            # Generate writemasks
            writemasks = []
            options = product(range(2), repeat=floats)
            for option in options:
                writemask = '0b' + bitmask
                for v in option:
                    writemask = writemask.replace('X', str(v), 1)
                writemask = int(writemask, 2)
                writemasks.append(writemask)
            
            # Transform
            result = [value & nullmask | writemask for writemask in writemasks]
            return result

        self.transform = transform

    def update_memory(self, line):
        address, value = line \
            .replace('mem[', '') \
            .replace(']', '') \
            .split(' = ', 1)
        address, value = int(address), int(value)
        addresses = self.transform(address)
        for address in addresses:
            self.memory[address] = value