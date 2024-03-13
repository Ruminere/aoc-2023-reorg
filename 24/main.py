import sys
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
import numpy as np
from collections import defaultdict, Counter, deque

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0

    hails = []
    with open(file) as fh:
        for line in fh:
            line = line.strip().split(" @ ")
            for i in rlen(line):
                line[i] = [int(j) for j in line[i].split(", ")]
            hails.append(line)
    ans1 = is_intersec(hails)
    
    print("1:", ans1)

# ==================================================

def is_intersec(hails):
    threshold = [200000000000000,200000000000000*2]
    # threshold = [7,27]

    ans = set()

    for i in rlen(hails):
        p1,s1 = hails[i]
        for j in range(i+1,len(hails)):
            p2,s2 = hails[j]
            try:
                l1 = [s1[0], -s2[0]]
                l2 = [s1[1], -s2[1]]
                a = [l1,l2]
                b = [p2[i]-p1[i] for i in rlen(a)]
                c = np.linalg.solve(a, b)
                if any(c[i]<0 for i in rlen(c)):
                    continue
                coord = [s1[i]*c[0] + p1[i] for i in rlen(a)]
                if all(threshold[0]<=coord[i]<=threshold[1] for i in rlen(coord)):
                    ans.add( (i,j) )
            except:
                continue
    return len(ans)

# ==================================================

main()