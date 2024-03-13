import sys, numpy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
from collections import defaultdict, Counter, deque

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    grid = ftg(file)

    ans1 = fire_beam(grid)
    ans2 = beam(grid)
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def beam(grid: list):
    dim = (len(grid),len(grid[0]))
    ans = 0
    for i in range(0,dim[0]):
        ans = max(ans, fire_beam(grid, ( (i,0), "R")))
        ans = max(ans, fire_beam(grid, ( (i,dim[1]-1), "L")))
    for i in range(0,dim[1]):
        ans = max(ans, fire_beam(grid, ( (0,i), "D")))
        ans = max(ans, fire_beam(grid, ( (dim[0]-1,i), "U")))
    return ans

dirs = {"U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)}

def get_next(grid: list, row: int, col: int, d: str):
    '''
    Takes a grid coordinate and returns the surrounding coordinates.
    '''
    if not in_bounds(grid, row, col):
        raise ValueError("grid coordinate is out of bounds")
    
    add = []
    current = grid[row][col]

    if current == ".":
        add.append(d)
        
    elif current == "/":
        if d == "R":
            add.append("U")
        elif d == "U":
            add.append("R")
        elif d == "L":
            add.append("D")
        elif d == "D":
            add.append("L")

    elif current == "\\":
        if d == "R":
            add.append("D")
        elif d == "U":
            add.append("L")
        elif d == "L":
            add.append("U")
        elif d == "D":
            add.append("R")

    elif current == "-":
        if d in "LR":
            add.append(d)
        elif d in "UD":
            add.append("L")
            add.append("R")
    
    elif current == "|":
        if d in "UD":
            add.append(d)
        elif d in "LR":
            add.append("U")
            add.append("D")

    ans = []
    for a in add:
        di = dirs[a]
        coord = (row+di[0], col+di[1])
        if in_bounds(grid, coord[0], coord[1]):
            ans.append((coord, a))

    return ans

def fire_beam(grid, start=((0,0),"R")):
    close = []
    progress = deque([start])
    while len(progress) > 0:
        current = progress.pop()
        coords = current[0]
        nbrs = get_next(grid, coords[0],coords[1],current[1])
        for nbr in nbrs:
            if nbr in close:
                continue
            progress.append(nbr)
        close.append(current)
    close_coords = set(c[0] for c in close)
    return len(close_coords)

def debug_ener(grid, close):
    close_coords = [c[0] for c in close]
    print(close_coords)
    a = ""
    for i in rlen(grid):
        for j in rlen(grid):
            if (i,j) in close_coords:
                a += "#"
                close_coords.remove( (i,j) )
            else:
                a += "."
        a += "\n"
    print(close_coords)
    return(a)

# ==================================================

main()