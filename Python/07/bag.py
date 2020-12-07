from functools import lru_cache

class Bag:
    def __init__(self, color, contents=[]):
        self.color = color
        self.contents = contents

    @lru_cache
    def find(self, color):
        if self.color == color:
            return True
        else:
            return any([content.find(color) for content in self.contents])

    def count(self):
        count = 1
        count += sum([content.count() for content in self.contents])
        return count

class BagFactory:
    def __init__(self, input):
        self.rules = BagFactory.parse_rules(input)

    @staticmethod
    def parse_rules(input):
        rules = input.split('\n')
        result = {}
        for rule in rules:
            rule = rule.replace('bags', 'bag').replace('.', '') # normalize plural, remove period
            parent, children = rule.split(' contain ', 1)
            parent = parent.replace(' bag', '')
            
            subresult = []
            children = children.split(', ')
            for child in children:
                child = child.replace(' bag', '')
                if child == 'no other':
                    continue
                else:
                    quantity = int(child[0])
                    color = child[2:]
                    for i in range(quantity):
                        subresult.append(color)
            
            result[parent] = subresult
        return result

    @lru_cache
    def generate_bag(self, color):
        bag = Bag(color)
        contents = self.rules[color]
        bag.contents = [self.generate_bag(content) for content in contents]
        return bag