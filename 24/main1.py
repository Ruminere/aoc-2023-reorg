import sys
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
import numpy as np
import sympy as sp
from collections import defaultdict, Counter, deque

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans2 = 0

    hails = []
    with open(file) as fh:
        for line in fh:
            line = line.strip().split(" @ ")
            for i in rlen(line):
                line[i] = [int(j) for j in line[i].split(", ")]
            hails.append(line)
    ans2 = is_intersec(hails)
    
    print("2:", ans2)

# ==================================================

def is_intersec(hails):
    p = sp.symbols("x,y,z")
    s = sp.symbols("dx,dy,dz")
    t = sp.symbols("t1,t2,t3")

    p1,s1 = hails[0]
    p2,s2 = hails[1]
    p3,s3 = hails[2]

    eqs = []
    for i in range(3):
        eqs.append(sp.Eq(s1[i]*t[0]+p1[i], s[i]*t[0]+p[i]))
    for i in range(3):
        eqs.append(sp.Eq(s2[i]*t[1]+p2[i], s[i]*t[1]+p[i]))
    for i in range(3):
        eqs.append(sp.Eq(s3[i]*t[2]+p3[i], s[i]*t[2]+p[i]))

    sol = sp.solve(eqs)[0]
    return sum(sol[i] for i in p)

# ==================================================

main()