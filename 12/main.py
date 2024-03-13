import sys
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as its

def main():
    testing = 0
    filename = "actual" if not testing else "test"

    ans1 = 0
    ans2 = 0

    lines = []
    with open(filename + ".in") as fh:
        for line in fh:
            line = line.strip()
            lines.append(line)

    for line in lines:
        spring_raw, cont_raw = line.split()
        cont_raw = [int(i) for i in cont_raw.split(",")]
        spring = spring_raw
        cont = [i for i in cont_raw]
        for _ in range(4):
            spring += "?" + spring_raw
            cont.extend(cont_raw)

        ans1 += num_arrangements(spring_raw, cont_raw, 0,0,0)
        calculated.clear()
        ans2 += num_arrangements(spring, cont, 0,0,0)
        calculated.clear()
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

calculated = {}
def num_arrangements(spring, cont, i, ci, l):
    '''
    i spring index
    ci container index
    l damaged length
    '''
    key = (i,ci,l)

    if key in calculated:
        return calculated[key]
    
    if i == len(spring): # end
        if ci == len(cont)-1 and l == cont[ci]:
            return 1
        if ci == len(cont) and l == 0:
            return 1
        return 0

    ans = 0
    if spring[i] in [".", "?"]: # good
        if l == 0: # repeated .
            ans += num_arrangements(spring, cont, i+1, ci, 0)
        elif ci < len(cont) and l == cont[ci]: # end of damaged segment
            ans += num_arrangements(spring, cont, i+1, ci+1, 0)
    if spring[i] in ["#", "?"]: # damaged
        ans += num_arrangements(spring, cont, i+1, ci, l+1)
    
    calculated[key] = ans
    return ans

# ==================================================

main()