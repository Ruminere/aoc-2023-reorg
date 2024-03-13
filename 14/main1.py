import sys, numpy, copy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as its

def main():
    testing = 0
    filename = "actual" if not testing else "test"

    grid = ftg(filename)

    ans2 = calc(grid)

    print("2:", ans2)

# ==================================================

def calc(grid):
    state = []
    for i in range(1000000000):
        for _ in range(4):
            shift(grid)
            grid = grid_rotate(grid)
        if grid in state:
            idx = state.index(grid)
            idx = (1000000000-idx) % (i-idx) + idx - 1
            return score(state[idx])
        g = copy.deepcopy(grid)
        state.append(g)
    return score(grid)

def shift(grid):
    for j in rlen(grid[0]):
        k = 0
        for i in rlen(grid):
            if grid[i][j] == "#":
                k = i + 1
            if grid[i][j] == "O":
                grid[i][j] = "."
                grid[k][j] = "O"
                k += 1

def score(grid):
    ans = 0
    for i in rlen(grid):
        ans += (len(grid)-i) * grid[i].count("O")
    return ans

# ==================================================

main()