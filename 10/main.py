import sys
sys.path.append('../')
from aoctools.aoc_functions import *

'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
'''

def main():
    testing = 0
    filename = "actual" if not testing else "test"

    ans1 = 0
    ans2 = 0

    grid = ftg(filename)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = (i,j)
                break
    
    raw = bfs(grid, start)
    ans1 = raw[0]

    loop = list(raw[1].keys())
    clean_grid(grid, loop)
    # grid_print(grid)

    ans2 = find_enclosed(grid, loop)

    print("1:", ans1)
    print("2:", ans2)

# ==================================================

dirs = {"|": [(-1,0),(1,0)],
        "-": [(0,-1),(0,1)],
        "L": [(-1,0),(0,1)],
        "J": [(-1,0),(0,-1)],
        "7": [(1,0),(0,-1)],
        "F": [(1,0),(0,1)],
        ".": [],
        "S": [(-1,0),(1,0),(0,-1),(0,1)]}

d = {(-1,0):(1,0),
     (1,0):(-1,0),
     (0,1):(0,-1),
     (0,-1):(0,1)}

def gcn(grid: list, row: int, col: int, sign: str):
    '''
    Takes a grid coordinate and returns the surrounding coordinates.
    '''
    if not in_bounds(grid, row, col):
        raise ValueError("grid coordinate is out of bounds")

    ans = []
    
    # print("current", (row,col), dirs[sign])
    for coord in d.keys():
        
        if coord not in dirs[sign]:
            continue
        row_new = row + coord[0]
        col_new = col + coord[1]
        if not in_bounds(grid, row_new, col_new):
            # print("oob")
            continue
        sign_new = grid[row_new][col_new]
        # print((row_new, col_new), dirs[sign_new])
        if d[coord] in dirs[sign_new]:
            ans.append( (row_new, col_new) )
    return ans

def bfs(grid, start):
    '''
    start is a grid coordinate
    '''
    to_explore = []
    dist = {}
    to_explore.append(start)
    dist[start] = 0
    while len(to_explore) > 0:
        current = to_explore.pop(0)
        nbrs = gcn(grid, current[0], current[1], grid[current[0]][current[1]])
        for nbr in nbrs:
            nbr_dist = dist[current] + 1
            if nbr not in dist.keys():
                dist[nbr] = nbr_dist
                to_explore.append(nbr)
            if dist[nbr] > nbr_dist:
                dist[nbr] = nbr_dist
    high = -float("inf")
    for val in dist.values():
        if val > high:
            high = val
    return high, dist

def clean_grid(grid, loop):
    '''
    Modifies grid.
    '''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j) not in loop:
                grid[i][j] = "."

def find_enclosed(grid, loop):
    enclosed = []
    for i in range(len(grid)):
        print(i)
        for j in range(len(grid[i])):
            if not grid[i][j] == "." or not is_bounded(grid, loop, i, j):
                continue
            if is_enclosed(grid, i, j):
                enclosed.append((i,j))
    # print("enclosed", enclosed)
    return len(enclosed)
            
def is_bounded(grid, loop, row, col):
    dd = d.keys()
    for ddd in dd:
        row_new = row
        col_new = col
        while True:
            row_new += ddd[0]
            col_new += ddd[1]
            if not in_bounds(grid,row_new,col_new):
                return False
            if (row_new, col_new) in loop:
                break
    return True

def is_enclosed(grid, row, col):
    ddd = (0,-1)
    row_new = row
    col_new = col
    count = 0
    while True:
        row_new += ddd[0]
        col_new += ddd[1]
        # if row == 3 and col == 14:
        #     print(row_new,col_new)
        if not in_bounds(grid,row_new,col_new):
            break
        valid = ["|","L","J","S"]
        # if row == 3 and col == 14:
        #     print(grid[row_new][col_new])
        if grid[row_new][col_new] in valid:
            # if row == 3 and col == 14:
            #     print("valid")
            count += 1
    # if row == 3 and col == 14:
    #     print(count)
    return count % 2 != 0    

# ==================================================

main()