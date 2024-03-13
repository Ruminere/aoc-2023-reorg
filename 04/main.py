import sys

def __main__():
    filename = "actual"
    fh = open(filename + ".in")
    ans1 = 0
    ans2 = 0

    games = []
    card_repeats = {}
    current_game = 0
    for line in fh:
        current_game += 1
        raw = line.strip()
        raw = raw.split(": ")[1]
        game_raw = raw.split(" | ")
        win = parse_raw(game_raw, 0)
        card = parse_raw(game_raw, 1)

        # part 1
        ans1 += calculate_points(win, card)

        # part 2
        card_repeats[current_game] = card_repeats.get(current_game, 0) + 1
        extend = calculate_wins(win, card)
        for i in range(1, extend+1): # count copies
            card_repeats[current_game + i] = card_repeats.get(current_game + i,0) + card_repeats[current_game]
    fh.close()

    ans2 = sum(card_repeats.values())
    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def parse_raw(game_raw, num):
    ans_raw = game_raw[num].split(" ")
    ans = []
    for i in ans_raw:
        if not len(i) == 0:
            ans.append(int(i))
    return ans
    
def calculate_points(win, card):
    exp = 0
    for num in card:
        if num in win:
            exp += 1
    if exp == 0:
        return 0
    else:
        return 2 ** (exp - 1)
    
def calculate_wins(win, card):
    exp = 0
    for num in card:
        if num in win:
            exp += 1
    return exp

# ==================================================

__main__()