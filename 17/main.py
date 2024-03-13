import sys, numpy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
from collections import defaultdict, Counter, deque

part = 1

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    grid = ftg(file, to_int=True)

    ans1 = dijkstra(grid)
    global part
    part = 2
    ans2 = dijkstra(grid)
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def get_neighbors(grid: list, row: int, col: int, curr_dir: str, times: int):
    '''
    At most 3 times in single direction
    '''
    if not in_bounds(grid, row, col):
        raise ValueError("grid coordinate is out of bounds")
    
    coords = []
    keys = {"U":0,"L":1,"D":2,"R":3}
    for key in keys:
        # no reverse
        if curr_dir != "" and (keys[key]+2)%4 == keys[curr_dir]:
            continue
        # direction step check
        if part == 1 and (key == curr_dir and times == 3):
            continue
        if part == 2 and curr_dir != "":
            if key == curr_dir and times == 10:
                continue
            if key != curr_dir and times < 4:
                continue
        t = times + 1 if key == curr_dir else 1
        coord = directions[key]
        row_new = row + coord[0]
        col_new = col + coord[1]
        if in_bounds(grid, row_new, col_new):
            coords.append( ((row_new, col_new),key,t) )
    return coords

def dijkstra(grid):
    start = (0,0)
    end = (len(grid)-1, len(grid[0])-1)

    close = set()
    dist = {(start,"",0):0} # coord dir dirtimes: cost
    while len(dist) > 0:
        current = min(dist, key=dist.get)
        cost = dist.pop(current)

        if current[0] == end:
            if part == 1:
                return cost
            elif part == 2:
                if 4<=current[2]<=10:
                    return cost
                else:
                    continue
        
        close.add(current)
        
        nbrs = get_neighbors(grid, *current[0], current[1], current[2])
        for n in nbrs:
            if n in close:
                continue
            nbr = n[0]
            nbr_cost = cost + grid[nbr[0]][nbr[1]]
            if n not in dist or nbr_cost < dist[n]:
                dist[n] = nbr_cost
    
    return cost
# ==================================================

main()