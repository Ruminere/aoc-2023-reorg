import sys, numpy
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
from collections import defaultdict, Counter, deque

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans2 = 0

    instrs = {}
    vals = []
    mode = 0
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            # print(line)
            if len(line) == 0:
                break
                mode = 1
            elif mode == 0:
                line = line.strip("}")
                k = line[:line.find("{")]
                d = line[line.find("{")+1:].split(",")
                ins = [i.split(":") for i in d]
                instrs[k] = ins
            elif mode == 1:
                line = line.strip("{").strip("}").split(",")
                val = {l[0]:int(l[2:]) for l in line}
                vals.append(val)
    
    # print(instrs)

    ans2 = parse_instrs(instrs)
    
    print("2:", ans2)

# ==================================================

def parse_instrs(instrs):
    b = [[1,4000] for i in "xmas"]
    b.insert(0,"in")
    bins = deque([b])
    good = []

    while bins:
        b = bins.popleft()
        # print("\ncurrent bin", b)

        k = b[0]
        # print("k", k)
        if k == "A":
            good.append(b)
        if k in "AR":
            continue

        ins = instrs[k]
        # print("ins", ins)
        for t in ins:
            if len(t) == 1:
                b[0] = t[0]
                # print("simple map",b)
                bins.append(b)
                continue
            b = split_bins(t,b)
            if len(b) == 2:
                bins.append(b[0]) #b0 is processed
                b = b[1]
            else:
                b = b[0]
        # print("queue:", bins)
    # print(good)
    ans = 0
    for b in good:
        a = 1
        for i in range(1,len(b)):
            a *= b[i][1] - b[i][0] + 1
        ans += a
    return ans


def split_bins(t, b):
    m = {"x":1,"m":2,"a":3,"s":4}
    cond = t[0]
    c = m[cond[0]]
    i = int(cond[2:])

    # print("t",t)
    # print("b",b)
    # print("c",c)

    if cond[1] == ">":
        if b[c][1] <= i:
            b[0] = t[1]
            # print("unsplit:",b)
            return [b]
        b0 = copy.deepcopy(b)
        b1 = copy.deepcopy(b)
        b0[c][0] = i+1
        b1[c][1] = i
        b0[0] = t[1]
        
    elif cond[1] == "<":
        if b[c][0] >= i:
            # print("unsplit:",b)
            return [b]
        b0 = copy.deepcopy(b)
        b1 = copy.deepcopy(b)
        b0[c][1] = i-1
        b1[c][0] = i
        b0[0] = t[1]
    
    # print("split:",b0,b1)
    return b0,b1
    
# ==================================================

main()