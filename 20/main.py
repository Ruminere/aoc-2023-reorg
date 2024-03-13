import sys
sys.path.append('../')
from aoctools.aoc_functions import *
import numpy as np
import itertools as it
from collections import defaultdict, Counter, deque

def main():
    testing = 1
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 0
    ans2 = 0

    instrs = {}
    flips = set()
    conjs = set()
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line[0] == "%":
                flips.add(line[1:line.find(" ")])
            elif line[0] == "&":
                conjs.add(line[1:line.find(" ")])
            else: # broadcast
                flips.add(line[:line.find(" ")])

            line = line.split(" -> ")
            line[0] = line[0].strip("%").strip("&")
            line[1] = line[1].split(", ")
            instrs[line[0]] = line[1]
    
    print("instrs", instrs, "\nflips", flips, "\nconjs", conjs)

    ans1 = find_pulse(instrs, flips, conjs)
    
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

statuses = []
conj_lows = []
lows = []
highs = []

def find_pulse(instrs, flips, conjs):
    times = 1000
    for _ in range(times):
        new_cycle = pulse(instrs, flips, conjs)
        if not new_cycle:
            break
    cycle = len(statuses)
    l = sum(lows) * (times // cycle) + sum(lows[:times%cycle])
    h = sum(highs) * (times // cycle) + sum(highs[:times%cycle])
    return l * h

'''
Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules; they initially default to remembering a low pulse for each input. When a pulse is received, the conjunction module first updates its memory for that input. Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
'''
    
def pulse(instrs, flips, conjs):
    status = {f:0 for f in flips} # 0 off 1 on
    conj_low = {f:True for f in conjs} # remembers if send low
    low = 0
    high = 0

    q = deque(["broadcaster"])
    while q:
        cur = q.popleft()
        targets = instrs[cur]
        print(cur, targets)
        if cur in flips:
            if not status[cur]:
                continue
            for target in targets:
                q.append(target)
                if target in flips:
                    if status[cur]:
                        status[target] = (status[target] + 1) % 2
                        low += 1
                    else:
                        high += 1
                else:
                    if status[cur]:
                        conj_low[target] = False
                        low += 1
                    else:
                        high += 1
                
        else: # conjs
            for target in targets:
                q.append(target)
                if target in flips:
                    if conj_low[cur]:
                        status[target] = (status[target] + 1) % 2 
                        low += 1
                    else:
                        high += 1
                else:
                    if conj_low[cur]:
                        conj_low[target] = False 
                        low += 1
                    else:
                        high += 1

    if status in statuses:
        return False
    else:
        statuses.append(status)
        conj_lows.append(conj_low)
        lows.append(low)
        highs.append(high)
        return True

# ==================================================

main()