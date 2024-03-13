'''
Python code for the second part of question 21.
'''
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

    # setup the grid from the input
    grid = ftg(file)
    for i in rlen(grid):
        for j in rlen(grid[i]):
            if grid[i][j] == "S":
                start = (i,j)
                break
    
    nums = bfs(grid,start)

    # # plotting for visualization purposes - this is what made me realize that the graph was likely quadratic
    # plt.title("Number of Possible Positions after Steps")
    # plt.xlabel("Steps")
    # plt.ylabel("Possible Positions")
    # plt.plot(nums)
    # plt.savefig("nums.png")

    # # === Wolfram stuff ===
    # # gives you the exact format you need to paste into this site:
    # # https://www.wolframalpha.com/input?i=interpolating+polynomial+calculator
    # s = "{"
    # for i in rlen(nums):
    #     if i % 131 in [65]:
    #         s += ("{%d,%d}," % (i,nums[i]))
    # s = s[:len(s)-1] + "}"
    # print(s)

    # # replace a, b, c with the coefficients that Wolfram gives you for your input
    # a = 14812/17161
    # b = 29615/17161
    # c = 2524/17161
    # f = lambda x: int(a*x**2 + b*x + c)
    # ans2 = f(26501365)

    # === numpy stuff ===
    # this code automatically does the calculations so you don't need to go to an external site
    x = list(filter(lambda i: i % 131 == 65, rlen(nums)))
    y = [nums[i] for i in x]
    p = poly.polyfit(x,y,2)
    ans2 = int(poly.polyval(26501365,p))-1

    print("2:", ans2)

# ==================================================

def gn(grid: list, row: int, col: int):
    '''
    Short for "grid neighbors"; modified from the function found in aoctools.
    
    Takes a grid coordinate and returns surrounding coordinates. To make the function more flexible for the purposes of the problem, coordinates can take on values that are outside the dimensions of the grid.
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
    '''
    Returns an array of the total number of plots that the elf can reach over a range of steps.
    '''
    to_explore = deque()
    to_explore.append(start)
    nums = [0] # stores the number of possible plot locations after every step
    for i in range(1,131*2+66):
        to_explore_new = deque()
        while to_explore:
            current = to_explore.popleft()
            nbrs = gn(grid, *current)
            for nbr in nbrs:
                simple = (nbr[0]%131, nbr[1]%131) # accounts for being outside the primary grid
                if grid[simple[0]][simple[1]] == "#": # don't add to queue if rock
                    continue
                to_explore_new.append(nbr)
        to_explore = deque(set(to_explore_new))
        nums.append(len(to_explore))
    return nums

# ==================================================

if __name__ == '__main__':
    main()