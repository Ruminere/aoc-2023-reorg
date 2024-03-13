import sys
sys.path.append('../')
from aoctools.aoc_functions import *

def main():
    filename = "actual"

    ans1 = 0
    ans2 = 0
    
    lines = []
    with open(filename + ".in") as fh:
        for line in fh:
            lines.append(raw_to_int(line.strip()))
    
    total = lmap(predict, lines)
    ans1 = sum([num[1] for num in total])
    ans2 = sum([num[0] for num in total])

    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def predict(nums):
    storage = []
    storage.append(nums)
    while not is_equal(storage[-1]):
        current = storage[-1]
        new = []
        for i in range(len(current)-1):
            new.append(current[i+1] - current[i])
        storage.append(new)
    for i in range(len(storage)-1, 0, -1):
        storage[i-1].insert(0, storage[i-1][0] - storage[i][0])
        storage[i-1].append(storage[i-1][-1] + storage[i][-1])
    return storage[0][0], storage[0][-1]

def is_equal(nums):
    num = nums[0]
    for n in nums:
        if n != num:
            return False
    return True

# ==================================================

main()