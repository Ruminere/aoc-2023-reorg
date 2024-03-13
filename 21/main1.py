import sys
sys.path.append('../')
from aoctools.aoc_functions import *
import numpy.polynomial.polynomial as poly
import itertools as it
from collections import defaultdict, Counter, deque
import matplotlib.pyplot as plt

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans2 = 0

    grid = ftg(file)
    for i in rlen(grid):
        for j in rlen(grid[i]):
            if grid[i][j] == "S":
                start = (i,j)
                break
    
    nums = bfs(grid,start)

    # plt.plot(nums)
    # plt.savefig("nums.png")

    # === Wolfram stuff ===
    # s = "{"
    # for i in rlen(nums):
    #     if i % 131 in [65]:
    #         s += ("{%d,%d}," % (i,nums[i]))
    # s = s[:len(s)-1] + "}"
    # print(s)

    # f = lambda x: int((14812 * x**2)/17161 + (29615*x)/17161 + 2524/17161)
    # ans2 = f(26501365)

    # === numpy stuff ===
    x = []
    y = []
    for i in rlen(nums):
        if i % 131 == 65:
            x.append(i)
            y.append(nums[i])
    p = poly.polyfit(x,y,2)
    ans2 = int(poly.polyval(26501365,p))-1

    print("2:", ans2)

# ==================================================

def gn(grid: list, row: int, col: int):
    '''
    Takes a grid coordinate and returns either:
    - surrounding coordinates, or
    - surrounding values.
    '''
    coords = []
    keys = ["U","D","L","R"]
    for key in keys:
        coord = directions[key]
        row_new = row + coord[0]
        col_new = col + coord[1]
        coords.append( (row_new, col_new) )
    return coords

def bfs(grid, start):
    to_explore = deque()
    to_explore.append(start)
    nums = [0]
    for i in range(1,131*2+66):
        to_explore_new = deque()
        while to_explore:
            current = to_explore.popleft()
            nbrs = gn(grid, *current)
            for nbr in nbrs:
                simple = (nbr[0]%131, nbr[1]%131)
                if grid[simple[0]][simple[1]] == "#":
                    continue
                to_explore_new.append(nbr)
        to_explore = deque(set(to_explore_new))
        nums.append(len(to_explore))
    return nums

# ==================================================

main()