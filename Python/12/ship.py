class Ship:
    def __init__(self):
        self.direction = (1, 0)
        self.position = (0, 0)
        self.cardinals = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0)
        }
        self.rotation = {'L': -1, 'R': 1}
    
    def turn(self, char, magnitude):
        vectors = list(self.cardinals.values())
        index = vectors.index(self.direction)
        turns = magnitude // 90
        self.direction = vectors[(index + self.rotation[char] * turns) % 4]

    def move(self, instruction):
        char, magnitude = instruction
        if char in self.rotation:
            self.turn(char, magnitude)
        else:
            direction = self.cardinals[char] if char in self.cardinals else self.direction
            x, y = [d * magnitude for d in direction] 
            self.position = (self.position[0] + x, self.position[1] + y)

class Waypoint:
    def __init__(self):
        self.position = (10, 1)
        self.cardinals = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0)
        }
        self.rotation = {'L': 1, 'R': -1} # Clockwise is negative
    
    def rotate(self, char, magnitude):
        vectors = list(self.cardinals.values())
        direction = self.rotation[char]
        turns = (magnitude // 90 * direction) % 4
        for i in range(turns):
            x, y = self.position
            self.position = -y, x

    def transport(self, ship, magnitude):
        vx, vy = [p * magnitude for p in self.position] 
        x, y = ship.position
        ship.position = x + vx, y + vy

    def move(self, instruction):
        char, magnitude = instruction
        if char in self.rotation:
            self.rotate(char, magnitude)
        elif char in self.cardinals:
            direction = self.cardinals[char]
            x, y = [d * magnitude for d in direction] 
            self.position = (self.position[0] + x, self.position[1] + y)


    
