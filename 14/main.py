import sys, numpy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as its

def main():
    testing = 0
    filename = "actual" if not testing else "test"

    grid = ftg(filename)

    rounded = []
    cubed = []
    for i in rlen(grid):
        for j in rlen(grid[i]):
            if grid[i][j] == "O":
                rounded.append( [i,j] )
            elif grid[i][j] == "#":
                cubed.append( (i,j) )
    
    ans1 = calc(grid, rounded, cubed)
        
    print("1:", ans1)

# ==================================================

def calc(grid, rounded, cubed):
    ans = 0
    for i in rlen(grid[0]):
        vals = shift(grid, rounded, cubed, i)
        for key, val in vals.items():
            for j in range(key[0]+1,key[0]+1+val):
                ans += len(grid)-j
    return ans

def shift(grid, rounded, cubed, col):
    col_cubed = [(-1,col)]
    for i in cubed:
        if i[1] == col:
            col_cubed.append(i)
    col_cubed.append((len(grid),col))
    
    col_rounded = []
    for i in rounded:
        if i[1] == col:
            col_rounded.append(i)

    push = {}
    for r in col_rounded:
        key = (-1,0)
        for i in rlen(col_cubed):
            if r[0] < col_cubed[i][0]:
                key = col_cubed[i-1]
                push[key] = push.get(key,0) + 1
                break
    return push

# ==================================================

main()