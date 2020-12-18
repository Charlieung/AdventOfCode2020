import numpy as np
# from dataclasses import dataclass, asdict
from collections import namedtuple
# import numba
# @numba.experimental.jitclass([
#     ('x', numba.int64),
#     ('y', numba.int64),
#     ('z', numba.int64),
#     ('active', numba.boolean),
# ])

# @dataclass
# class Coordinates:
#     x: int
#     y: int
#     z: int

Coordinates = namedtuple('Coordinates', ['x', 'y', 'z'])

class Cube:
    def __init__(self, coordinates, active=False):
        self.coordinates = coordinates
        self.neighbors = []
        self.active = active
        self.change = False

        x, y, z = list(coordinates)
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                for k in range(z - 1, z + 2):
                    if (i, j, k) != (x, y, z):
                        self.neighbors.append(Coordinates(i, j, k))

class Grid:
    def __init__(self, initial_state):
        """Initial state is on z = 0
        This assumption doesn't matter on infinite grid"""
        self.cubes = {}

        xs, ys = np.where(initial_state)
        xs, ys = xs.tolist(), ys.tolist()
        for x, y in zip(xs, ys):
            coordinates = Coordinates(x, y, 0)
            cube = Cube(coordinates, active=True)
            self.cubes[coordinates] = cube
            self.append_neighbors(cube)
    
    def __repr__(self):
        active_cubes = [cube for cube in self.cubes.values() if cube.active]
        xs, ys, zs = [], [], []
        for cube in active_cubes:
            # print(cube.coordinates)
            x, y, z = list(cube.coordinates)
            xs.append(x)
            ys.append(y)
            zs.append(z)
        xs, ys, zs = np.array(xs), np.array(ys), np.array(zs)
        # Zero out coordinates
        xs -= np.min(xs)
        ys -= np.min(ys)
        zs -= np.min(zs)
        max_bounds = np.max(xs) + 1, np.max(ys) + 1, np.max(zs) + 1
        cube_matrix = np.zeros(max_bounds)

        for i in range(len(active_cubes)):
            x, y, z = xs[i], ys[i], zs[i]
            cube_matrix[x, y, z] = 1
        
        result = '\n\n'
        for z in set(zs):
            result += f'z = {z}'
            result += '\n'
            result += np.array_str(
                cube_matrix[:,:,z]
            ).replace('.', '') \
                .replace(' [', '') \
                .replace('[', '') \
                .replace(']', '') \
                .replace('0', '.') \
                .replace('1', '#')
            result += '\n\n'
            # print(cube_matrix[:,:,z][0])
        result += '========================'
        return result

    def append_neighbors(self, cube):
        for neighbor in cube.neighbors:
            if neighbor not in self.cubes:
                self.cubes[neighbor] = Cube(neighbor)

    def count_active_neighbors(self, cube):
        active_count = sum([self.cubes.get(neighbor).active \
            for neighbor in cube.neighbors if neighbor in self.cubes])
        return active_count
    
    def cycle(self):
        neighbor_queue = []
        active_count_array = [
            self.count_active_neighbors(cube) \
                for cube in self.cubes.values()
            ]

        for active_neighbors, cube in \
            zip(active_count_array, self.cubes.values()):

            if cube.active:
                cube.active = active_neighbors in [2, 3]
            else:
                cube.active = active_neighbors == 3
                if cube.active:
                    neighbor_queue.append(cube)
        
        while neighbor_queue:
            cube = neighbor_queue.pop()
            self.append_neighbors(cube)

    def count_active_cubes(self):
        return sum([cube.active for cube in self.cubes.values()])