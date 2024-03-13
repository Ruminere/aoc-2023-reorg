import sys
sys.path.append('../')
from aoctools.aoc_functions import *
from collections import Counter

part = 1

def __main__():
    filename = "actual"
    fh = open(filename + ".in")
    ans1 = 0
    ans2 = 0
    
    n = 0
    hands = []
    for line in fh:
        raw = line.strip().split()
        hands.append( [raw[0], int(raw[1])] )
    fh.close()
    
    ans1 = calculate_winnings(hands)
    global part
    part = 2
    ans2 = calculate_winnings(hands)

    print("1:", ans1)
    print("2:", ans2)

# ==================================================

def calculate_winnings(hands):
    for hand in hands:
        determine_type(hand)

    hands.sort(key=lambda hands: hands[-1])

    order(hands)
    return winnings(hands)

def determine_type(hand):
    '''
    5, 4, 3, 2, 1 in order
    simply appends stuff to the end of hand
    '''
    hist = Counter(hand[0])
    joker = 0
    if part == 2:
        joker = hist["J"]
        del hist["J"]
        
    
    vals = list(hist.values())
    vals.sort(reverse=True)
    if len(vals) == 0 or vals[0]+joker == 5: # five kind
        hand.append(7)
    elif vals[0]+joker == 4: # four kind
        hand.append(6)
    elif vals[0]+joker == 3: # full house
        hand.append(5) if vals[1] == 2 else hand.append(4)
    elif vals[0]+joker == 2: # two/one pair
        hand.append(3) if vals[1] == 2 else hand.append(2)
    else:
        hand.append(1) # high card

def split_tie(hand1, hand2):
    '''
    1 if hand1 is worse else 2
    '''
    ranks = "AKQJT98765432" if part == 1 else "AKQT98765432J"
    card1 = hand1[0]
    card2 = hand2[0]
    for i in range(len(card1)):
        if ranks.find(card1[i]) > ranks.find(card2[i]):
            return 1
        elif ranks.find(card1[i]) < ranks.find(card2[i]):
            return 2
        else: # equal
            continue
    return -1 # all equal, should never reach this

def order(hands):
    while True:
        swap_count = 0
        for i in range(len(hands)-1):
            card1 = hands[i]
            card2 = hands[i+1]
            if card1[-1] == card2[-1]:
                if split_tie(card1, card2) == 2:
                    swap_count += 1
                    hands[i] = card2
                    hands[i+1] = card1
        if swap_count == 0:
            break

def winnings(hands):
    total = 0
    for i in range(len(hands)):
        total += hands[i][1] * (i+1)
    return total

# ==================================================

__main__()