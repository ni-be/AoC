import linecache
from collections import Counter


def two_pairs(cards):
    cd = Counter(cards)
    x = list(cd.values())
    y = Counter(x)
    return y[2] == 2


def card_group(cards):
    cd = Counter(cards)
    if max(cd.values()) == 5:
        return 6
    elif max(cd.values()) == 4:
        return 5
    elif len(cd) == 2 and max(cd.values()) == 3:
        return 4
    elif max(cd.values()) == 3:
        return 3
    elif two_pairs(cards):
        return 2
    elif max(cd.values()) == 2:
        return 1
    else:
        return 0


def ranking(hand):
    cards = hand[0]
    ranked = [card_group(cards)]
    # print(ranked)
    for card in cards:
        ranked.append(fun_card_score(card))
    return tuple(ranked)


def ranking2(hand):
    cards = hand[0]
    best = 0
    for card in cards:
        j = cards.replace('J', str(card))
        best = max(best, card_group(j))

    lt = [best]
    for card in cards.replace('J', '1'):
        lt.append(fun_card_score(card))
    return tuple(lt)


def fun_card_score(card):
    return card_score[card]


# Attach to every card a value from 1 to 12 for ranking
CARDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
card_score = {str(k): i for i, k in enumerate(CARDS)}


def solve(input):
    lines = linecache.getlines(input)
    answer_p1 = 0
    answer_p2 = 0
    hands = []

    for line in lines:
        temp = []
        temp.append(line.split()[0])
        temp.append(int(line.split()[1]))
        hands.append(temp)

    hands2 = hands
    hands.sort(key=ranking)
    for i, (hds, bet) in enumerate(hands):
        answer_p1 += (i+1)*bet

    hands2.sort(key=ranking2)
    for i, (hds, bet) in enumerate(hands):
        answer_p2 += (i+1)*bet

    print(f"Answer 1: {answer_p1}")
    print(f"Answer 2: {answer_p2}")


solve('puzzle_input_7.txt')
# 248105065
# 249515436
