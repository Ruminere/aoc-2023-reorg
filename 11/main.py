import sys
sys.path.append('../')
from aoctools.aoc_functions import *

def main():
    testing = 0
    filename = "actual" if not testing else "test"

    ans1 = 0
    ans2 = 0

    grid = ftg(filename)

    row_expand = []
    col_expand = []
    for i in rlen(grid):
        if all(grid[i][j] == "." for j in rlen(grid[i])):
            row_expand.append(i)
    
    for j in rlen(grid):
        if all(grid[i][j] == "." for i in rlen(grid)):
            col_expand.append(j)

    galaxies = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                galaxies.append((i,j))

    ans1 = calc_dists(galaxies, row_expand, col_expand, 2)
    ans2 = calc_dists(galaxies, row_expand, col_expand, 10**6)
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def calc_dists(galaxies, row_expand, col_expand, expand):
    dists = []
    for i in rlen(galaxies):
        for j in range(i, len(galaxies)):
            one = galaxies[i]
            two = galaxies[j]
            dist = abs(two[1]-one[1]) + abs(two[0]-one[0])
            for r in row_expand:
                if r in range(min(one[0],two[0]),max(one[0],two[0])):
                    dist += expand-1
            for r in col_expand:
                if r in range(min(one[1],two[1]),max(one[1],two[1])):
                    dist += expand-1
            dists.append(dist)
    return sum(dists) 

# ==================================================

main()