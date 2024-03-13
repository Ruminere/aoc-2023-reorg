import sys

def __main__():
    filename = "actual"
    fh = open(filename + ".in")
    ans1 = 0
    ans2 = 0

    for line in fh:
        raw = line.strip()
        raw0 = raw.split(": ")
        game_id = int(raw0[0].split(" ")[1])
        
        raw1 = raw0[1].split("; ")
        records = []
        for raw2 in raw1:
            pairs = {}
            raw2 = raw2.split(", ")
            for pair in raw2:
                pair = pair.split(" ")
                pairs[pair[1]] = int(pair[0])
            records.append(pairs)
        
        possible = True
        for i in range(len(records)):
            if not is_possible(records[i]):
                possible = False
        if possible:
            ans1 += game_id

        ans2 += find_power(records)
        
        # print(game_id, records)
    fh.close()
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def is_possible(scenario):
    nums = {"red":12, "green":13, "blue":14}
    for key in scenario.keys():
        if scenario[key] > nums[key]:
            return False
    return True

def find_power(record):
    lowest = {"red":0, "green":0, "blue":0}
    for scenario in record:
        for key in scenario.keys():
            if scenario[key] > lowest[key]:
                lowest[key] = scenario[key]

    ans = 1
    for value in lowest.values():
        ans *= value
    return ans

# ==================================================

__main__()