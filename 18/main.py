import sys, numpy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
from collections import defaultdict, Counter, deque

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    dirs = {0:"R",1:"D",2:"L",3:"U"}

    c1s = []
    c2s = []
    with open(file) as fh:
        for line in fh:
            line = line.strip().split()
            c1s.append((line[0],int(line[1])))
            c = line[2].strip("(#").strip(")")
            c2s.append((dirs[int(c[-1])],int(c[:-1],16)))

    ans1 = dig(c1s)
    ans2 = dig(c2s)
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def polygon_area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

def dig(cmds):
    fill = [(0,0)]
    border = 0
    for cmd in cmds:
        d = directions[cmd[0]]
        d = tuple(i*cmd[1] for i in d)
        border += cmd[1]
        
        current = tuple(i for i in fill[-1])
        fill.append((current[0]+d[0],current[1]+d[1]))
    fill.pop()

    return int(polygon_area(fill) + border // 2 + 1)

# ==================================================

main()