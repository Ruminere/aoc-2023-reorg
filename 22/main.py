import sys
sys.path.append('../')
from aoctools.aoc_functions import *
import numpy as np
import itertools as it
from collections import defaultdict, Counter, deque

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    cubes = []
    with open(file) as fh:
        for line in fh:
            line = line.strip().split("~")
            for i in rlen(line):
                line[i] = tuple(line[i].split(","))
                line[i] = tuple(int(l) for l in line[i])
            cubes.append(tuple(line))
    cubes.sort(key=lambda x:x[0][2])

    cube_pos = drop(cubes)
    for i in rlen(cubes):
        current_falling = 0
        current = cubes[:i] + cubes[i+1:]
        current_cube_pos = drop(current)
        mod_cube_pos = copy.copy(cube_pos)
        mod_cube_pos.pop(cubes[i])
        for cube in current_cube_pos:
            if current_cube_pos[cube] != mod_cube_pos[cube]:
                current_falling += 1
        if current_falling == 0:
            ans1 += 1
        else:
            ans2 += current_falling

    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def drop(cubes):
    cube_pos = defaultdict(lambda:-1)
    max_z = defaultdict(lambda:-1)
    for cube in cubes:
        x_range = range(cube[0][0],cube[1][0]+1)
        y_range = range(cube[0][1],cube[1][1]+1)
        coords = list(it.product(x_range,y_range))
        height = cube[1][2]-cube[0][2]+1
        current_z = 0
        for coord in coords:
            c = max_z[coord]
            if c > current_z:
                current_z = c
        cube_pos[cube] = [current_z,current_z+height]
        for coord in coords:
            max_z[coord] = current_z + height
    return cube_pos

# ==================================================

main()