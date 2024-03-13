import math, re
import itertools
import os, sys, copy

# VARIABLES

directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "NW": (-1,-1),
    "NE": (1,-1),
    "SW": (-1,1),
    "SE": (1,1),
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "^": (-1, 0),
    "V": (1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

dirs = directions

# UTILITY

def lmap(func, *iterable):
    '''
    Shorthand for list(map(func, *iterable)).
    '''
    return list(map(func, *iterable))

def rsorted(iterable, key=None):
    '''
    Shorthand for sorted(iterable, reverse=True).
    '''
    return sorted(iterable, key=key, reverse=True)

def rlen(iterable, rev=False):
    '''
    Shorthand for range(len(iterable)).
    '''
    return range(len(iterable)) if not rev else range(len(iterable)-1,-1,-1)

# GRID FUNCTIONS

def grid_in_bounds(grid: list, row: int, col: int):
    '''
    Returns a boolean value indicating whether the desired grid coordinate is in bounds.
    '''
    dim = (len(grid), len(grid[0]))
    return row >= 0 and row < dim[0] and col >= 0 and col < dim[1]
in_bounds = grid_in_bounds

def grid_neighbors(grid: list, row: int, col: int, diagonal=True, actual=False):
    '''
    Takes a grid coordinate and returns either:
    - surrounding coordinates, or
    - surrounding values.
    '''
    if not in_bounds(grid, row, col):
        raise ValueError("grid coordinate is out of bounds")

    coords = []
    keys = ["U","D","L","R"]
    if diagonal:
        keys.extend(["NW","NE","SW","SE"])
    for key in keys:
        coord = directions[key]
        row_new = row + coord[0]
        col_new = col + coord[1]
        if in_bounds(grid, row_new, col_new):
            coords.append( (row_new, col_new) )
    if not actual:
        return coords
    else:
        return [grid[coord[0]][coord[1]] for coord in coords]
get_neighbors = grid_neighbors
gn = grid_neighbors

def file_to_grid(filename: str, start=0, to_int=False):
    '''
    Reads a file and converts it to a grid starting from the starting line. Converts to integers if the setting is on.
    '''
    grid = []
    file = filename
    file += ".in" if file[-3:] != ".in" else ""
    count = 0
    with open(file) as fh:
        for line in fh:
            if count < start:
                continue
            row = list(line.strip())
            if to_int:
                row = [int(val) for val in row]
            grid.append(row)
            count += 1
    return grid
ftg = file_to_grid

def grid_rotate(grid: list, times=1):
    '''
    Rotates the grid clockwise. Rotates once by default.
    '''
    tmp = copy.deepcopy(grid)
    for _ in range(times):
        tmp = [list(reversed(i)) for i in zip(*tmp)]
    return tmp

def grid_str(grid: list):
    '''
    Returns the string representation of a grid of characters.
    '''
    rowstr = ""
    for row in grid:
        for val in row:
            rowstr += str(val)
        rowstr += "\n"
    return rowstr

def grid_print(grid: list):
    '''
    Prints a grid of characters.
    '''
    print(grid_str(grid))

# STRING TO NUMBER COMPREHENSION

def raw_to_int(raw: str, neg=True):
    '''
    Returns a list of all integers in a string. Includes negative symbols by default.
    '''
    to_find = r"-?\d+" if neg else r"\d+"
    return [int(n) for n in re.findall(to_find, raw.strip())]
rti = raw_to_int

def raw_to_digits(raw: str, neg=True):
    '''
    Returns a list of all digits in a string. Includes negative symbols by default.
    '''
    to_find = r"-?\d" if neg else r"\d"
    return [int(n) for n in re.findall(to_find, raw.strip())]
raw_to_dig = raw_to_digits
rtd = raw_to_digits

def raw_to_float(raw: str, neg=True):
    '''
    Returns a list of all decimals in a string. Includes negative symbols by default.
    '''
    to_find = r"-?\d*\.?\d+" if neg else r"\d*\.?\d+"
    return [float(n) for n in re.findall(to_find, raw.strip())]
rtf = raw_to_float