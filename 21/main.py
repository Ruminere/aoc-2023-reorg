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

    grid = ftg(file)
    for i in rlen(grid):
        for j in rlen(grid[i]):
            if grid[i][j] == "S":
                start = (i,j)
                break

    ans1 = bfs(grid,start)
    
    print("1:", ans1)

# ==================================================

def bfs(grid, start):
    to_explore = deque()
    to_explore.append(start)
    for _ in range(64):
        to_explore_new = deque()
        while to_explore:
            current = to_explore.popleft()
            nbrs = gn(grid, *current, diagonal=False)
            for nbr in nbrs:
                if grid[nbr[0]][nbr[1]] == "#":
                    continue
                to_explore_new.append(nbr)
        to_explore = deque(set(to_explore_new))
    return len(to_explore)

# ==================================================

main()