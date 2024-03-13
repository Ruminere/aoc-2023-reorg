import sys, collections

def __main__():
    filename = "actual"
    fh = open(filename + ".in")
    ans1 = 0

    inp = [line.strip() for line in fh.readlines()]
    inp = [i for i in inp if len(i) != 0]
    seeds_raw = inp.pop(0)
    seeds_raw = [int(i) for i in seeds_raw.split(": ")[1].split()]
    # print(seeds_raw)
    # print(inp)

    seeds = []
    for seed in seeds_raw:
        seeds.append( [seed,False] )
    # for i in range(0, len(seeds_raw), 2):
    #     # print("Range", seeds_raw[i], seeds_raw[i+1])
    #     for j in range(seeds_raw[i], seeds_raw[i]+seeds_raw[i+1]):
    #         seeds.append( [j,False] )
    # print(seeds)

    for line in inp:
        if (line[0].isalpha()): # new category
            for seed in seeds:
                seed[1] = False
            # print(line[:-5])
            # print(seeds)
            continue
        nums = [int(i) for i in line.split()]
        # print(nums)
        for seed in seeds:
            # print("seed:", seed)
            if seed[0] in range(nums[1], nums[1]+nums[2]) and not seed[1]:
                seed[0] += nums[0] - nums[1]
                seed[1] = True
    ans1 = float("inf")
    for seed in seeds:
        if seed[0] < ans1:
            ans1 = seed[0]
    
    print("1:", ans1)

# ==================================================s

# ==================================================

__main__()