import sys, numpy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
from collections import defaultdict

def main():
    testing = 0
    filename = "actual" if not testing else "test"

    ans1 = 0
    ans2 = 0

    vals = open(filename + ".in").readlines()[0].strip().split(",")

    ans1 = sum(get_hash(n) for n in vals)
    ans2 = get_pow(vals)
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def get_hash(val: str):
    ans = 0
    for c in val:
        ans = (ans + ord(c)) * 17 % 256
    return ans

def get_pow(vals: list):
    boxes = defaultdict(dict)
    for val in vals:
        if "-" in val:
            label = val[:-1]
            boxes[get_hash(label)].pop(label,None)
        else:
            label, n = val.split("=")
            boxes[get_hash(label)][label] = int(n)
    return sum((i+1) * (s+1) * l for i in boxes for s,l in enumerate(boxes[i].values()))

# ==================================================

main()