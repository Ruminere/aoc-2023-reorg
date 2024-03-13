import sys, numpy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
from collections import defaultdict, Counter, deque

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans2 = 0

    grid = ftg(file)

    ans2 = bfs(grid)
    print("2:", ans2)

# ==================================================

def get_neighbors(grid: list, row: int, col: int):
    if not in_bounds(grid, row, col):
        raise ValueError("grid coordinate is out of bounds")
    
    coords = []
    keys = {"U":0,"L":1,"D":2,"R":3}
    for key in keys:
        coord = directions[key]
        row_new = row + coord[0]
        col_new = col + coord[1]
        if not in_bounds(grid, row_new, col_new):
            continue

        if grid[row_new][col_new] == "#":
            continue

        coords.append( (row_new, col_new) )
    return coords

def bfs(grid):
    start = (0,1)
    end = (len(grid)-1, len(grid[0])-2)

    longest = 0
    q = deque()
    q.append([start])
    while q:
        current = q.pop()

        if current[-1] == end:
            longest = max(len(current),longest)
            print(longest)
            continue
        
        nbrs = get_neighbors(grid, *current[-1])
        for nbr in nbrs:
            if (len(current) > 1 and nbr == current[-2]) or nbr in current:
                continue
            n = current.copy()
            n.append(nbr)
            q.append(n)
    
    return longest-1
# ==================================================

main()