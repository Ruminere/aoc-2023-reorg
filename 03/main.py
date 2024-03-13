import sys

part = 1

def __main__():
    filename = "actual"
    fh = open(filename + ".in")
    ans1 = 0
    ans2 = 0
    
    schematic = []
    for line in fh:
        raw = line.strip()
        row = [i for i in raw]
        schematic.append(row)
    fh.close()

    ans1 = get_nums(schematic)
    global part
    part = 2
    ans2 = get_nums(schematic)

    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def get_nums(schematic):
    ans = 0
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            current = schematic[i][j]
            if not current.isdigit() and current != ".":
                ans += search_part_number(schematic, (i,j))
    return ans

def search_part_number(schematic, coord):
    nums_raw = set()
    dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]

    for d in dirs:
        current = (coord[0]+d[0], coord[1]+d[1])
        if schematic[current[0]][current[1]].isdigit():
            num = measure_number(schematic, current)
            nums_raw.add(num)

    if part == 2 and len(nums_raw) != 2:
        return 0
    
    nums = []
    for num in nums_raw:
        ns = ""
        for i in range(num[1],num[2]):
            ns += schematic[num[0]][i]
        nums.append(int(ns))

    if part == 2:
        return nums[0] * nums[1]
    else:
        return sum(nums)
    
def measure_number(schematic, coord):
    current = [i for i in coord]
    # go left
    while True:
        current[1] += -1
        if current[1] < 0 or not schematic[current[0]][current[1]].isdigit():
            left = current[1] + 1
            break
    # go right
    while True:
        current[1] += 1
        if current[1] >= len(schematic[0]) or not schematic[current[0]][current[1]].isdigit():
            right = current[1]
            break
    return (coord[0],left,right)

# ==================================================

__main__()