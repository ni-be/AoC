import linecache
from math import lcm
# Day8


def dic_maker(input):
    command = []
    game = {}
    lines = linecache.getlines(input)
    akey = []
    zkey = []
    for i, line in enumerate(lines):
        if i == 0:
            for char in line:
                if char.isalpha():
                    command.append(char.strip())
        elif i > 1:
            key = line.split("=")[0].strip()
            pre_val = line.split("=")[1].strip().strip('(').strip(')')
            value = []
            value.append(pre_val.split(',')[0])
            value.append(pre_val.split(',')[1].strip(' '))
            game[key] = value
            if key[2] == 'A':
                akey.append(key)
                # print(key)
            elif key[2] == 'Z':
                zkey.append(key)
                # print(key)
    return command, game, akey, zkey


def play(cmd, key, game):
    if cmd == 'R':
        keys = game[key]
        next_key = keys[1]
        return next_key
    elif cmd == 'L':
        keys = game[key]
        next_key = keys[0]
        return next_key


def runner(zkey, akey, command, game):
    steps = 0
    while akey[2] != "Z":
        for cmd in command:
            steps += 1
            akey = play(cmd, akey, game)
    return steps


def solve_part2(input):
    steps = []
    command, game, akey, zkey = dic_maker(input)
    for key in akey:
        steps.append(runner(zkey, key, command, game))
    print(lcm(*steps))


def solve_part1(input):
    steps = 0
    nkey = 'AAA'
    command, game, akey, zkey = dic_maker(input)
    while nkey != 'ZZZ':
        for cmd in command:
            steps += 1
            nkey = play(cmd, nkey, game)
    print(steps)


solve_part1('puzzle_input_8.txt')
solve_part2('puzzle_input_8.txt')
