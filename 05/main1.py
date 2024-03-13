import sys, collections

def __main__():
    filename = "actual"
    fh = open(filename + ".in")
    ans2 = 0

    inp = [line.strip() for line in fh.readlines()]
    inp = [i for i in inp if len(i) != 0]
    seeds_raw = inp.pop(0)
    seeds_raw = [int(i) for i in seeds_raw.split(": ")[1].split()]
    # print(seeds_raw)
    inp.append("final stretch asufhudsifhidsfuh") # based on how the algorithm works
    # print(inp)

    seeds = []
    # for seed in seeds_raw:
    #     seeds.append( [seed,False] )
    for i in range(0, len(seeds_raw), 2):
        # print("Range", seeds_raw[i], seeds_raw[i+1])
        seeds.append([seeds_raw[i], seeds_raw[i]+seeds_raw[i+1], False])
    # print(seeds)

    groups = []
    for line in inp:
        if (line[0].isalpha()): # new category
            for seed in seeds:
                seed[2] = False
            # print("\n")
            # print("start:", line[:-5])
            # print("before split:", seeds)
            seeds = split_seeds(seeds, groups)
            # print("after split:", seeds)

            for group in groups:
                for seed in seeds:
                    # print("=====")
                    # print("group", group)
                    # print("seed", seed)
                    # print("low:", seed[0], group[1])
                    # print("high:", seed[1], group[1]+group[2])
                    if not seed[2] and seed[0] >= group[1] and seed[1] <= group[1]+group[2]:
                        seed[0] += group[0] - group[1]
                        seed[1] += group[0] - group[1]
                        seed[2] = True
            # print("after map:", seeds)
            groups = []
        else:
            groups.append([int(i) for i in line.split()])
        # print(nums)
        # for seed in seeds:
        #     print("seed:", seed)
        # if seed[0] in range(nums[1], nums[1]+nums[2]) and not seed[1]:
        #         seed[0] += nums[0] - nums[1]
        #         seed[1] = True
    ans2 = float("inf")
    # print(seeds)
    for seed in seeds:
        if seed[0] < ans2:
            ans2 = seed[0]
    
    print("2:", ans2)

# ==================================================

def split_seeds(original_seeds, groups):
    seeds = [i for i in original_seeds]
    for group in groups:
        new_seeds = []
        for seed in seeds:
            # print("=====")
            # print("group", group)
            # print("seed", seed)
            # print("low:", seed[0], group[1])
            # print("high:", seed[1], group[1]+group[2])

            seed_low = seed[0]
            seed_high = seed[1]
            group_low = group[1]
            group_high = group[1]+group[2]

            if seed_low >= group_low and seed_high <= group_high: # bounds already good
                # print("in range")
                new_seeds.append(seed)
                continue
            if seed_high <= group_low or seed_low >= group_high: # too low/high
                # print("out of bounds")
                new_seeds.append(seed)
                continue

            new_seed = [i for i in seed]
            if seed_low < group_low:
                # print("low split")
                new_seed[0] = group_low
                new_seeds.append([seed_low, group_low, new_seed[2]])
            if seed_high > group_high:
                # print("high split")
                new_seed[1] = group_high
                new_seeds.append([group_high, seed_high, new_seed[2]])
            new_seeds.append(new_seed)
        seeds = new_seeds
    return seeds

# groups = [[0, 3, 2]]
# print(split_seeds([[3,1,True]], groups))
# print(split_seeds([[1,4,True]], groups))
# print(split_seeds([[5,7,True]], groups))
# print(split_seeds([[4,7,False]], groups))

# ==================================================

__main__()