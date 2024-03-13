import sys
sys.path.append('../')
from aoctools.aoc_functions import *

def __main__():
    filename = "actual"
    fh = open(filename + ".in")
    ans1 = 1
    ans2 = 0
    
    temp1 = []
    temp2 = ["", ""]
    n = 0
    for line in fh:
        raw = line.strip().split()[1:]
        # 1
        temp1.append([int(i) for i in raw])
        
        for s in raw:
            temp2[n] += s
        n += 1
    fh.close()

    races = [(temp1[0][i], temp1[1][i]) for i in range(len(temp1[0]))]
    temp2 = [int(i) for i in temp2]
    num_wins1 = [calculate_wins(race) for race in races]

    for i in num_wins1:
        if i != 0:
            ans1 *= i
    ans2 = calculate_wins(temp2)

    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def calculate_wins(race):
    lower = 0
    s = 0
    while s < race[0]:
        if (race[0] - s) * s > race[1]:
            lower = s
            break
        s += 1

    upper = 0
    s = race[0]
    while s > 0:
        if (race[0] - s) * s > race[1]:
            upper = s
            break
        s -= 1

    return upper - lower + 1


# ==================================================

__main__()