from linecache import getlines


def calculator(row):
    diff = []
    for i, val in enumerate(row):
        rl = len(row) - 2
        try:
            if i != rl:
                diff.append(row[i+1]-row[i])
            elif row[i+1] != 'X':
                diff.append(row[i+1]-row[i])
        except IndexError:
            diff.append('X')
    return diff


def calcY(row):
    diff = []
    for i in range(1, len(row)):
        try:
            diff.append(row[i+1]-row[i])
        except IndexError:
            diff.insert(0, 'Y')
    return diff


def sum_array(nums):
    total = 0
    for num in nums:
        if not isinstance(num, str):
            total += num
    return total


def part1(rows):
    answer = 0
    for row in rows:
        sum_val = 1
        play = []
        row.append('X')
        play.append(row)
        while sum_val != 0:
            row = calculator(row)
            play.append(row)
            sum_val = sum_array(row)
        play[-1][-1] = 0
        for i in range(1, len(play)):
            play[-i-1][-1] = play[-i][-1] + play[-i-1][-2]
        answer += play[0][-1]
    print(answer)


def part2(rows):
    answer = 0
    for row in rows:
        sum_val = 1
        play = []
        row.insert(0, 'Y')
        play.append(row)
        while sum_val != 0:
            row = calcY(row)
            play.append(row)
            sum_val = sum_array(row)
        play[-1][0] = 0
        for i in range(1, len(play)):
            play[-i-1][0] = play[-i-1][1] - play[-i][0]
        answer += play[0][0]
    print(answer)


def solve():
    lines = getlines('puzzle_input_9.txt')
    rows = [[int(i) for i in line.split()] for line in lines]
    part1(rows)
    part2(rows)


solve()
