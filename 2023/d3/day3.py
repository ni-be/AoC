#!/usr/bin/python3

SYMBOLS = ['@', '#', '$', '%', '^', '&', '*',
           '/', '-', '+', '=', ':', ';', '<', '>']
MATRIX = []


def part2(y, x):
    directions = [(y-1, x), (y+1, x), (y, x-1), (y, x+1),
                  (y-1, x+1), (y+1, x-1), (y-1, x-1), (y+1, x+1)]
    value = []
    for direction in directions:
        temp = check(*direction)
        if temp > 0:
            value.append(temp)

    if len(value) == 2:
        return value[0] * value[1]


def part1(y, x):
    directions = [(y-1, x), (y+1, x), (y, x-1), (y, x+1),
                  (y-1, x+1), (y+1, x-1), (y-1, x-1), (y+1, x+1)]
    sum = 0
    for direction in directions:
        temp = check(*direction)
        sum += temp
    return sum


def check(y, x):
    i = 1
    j = 1
    if isinstance(MATRIX[y][x], int):
        temp = str(MATRIX[y][x])
        # temp = ''
        try:
            while isinstance(MATRIX[y][x-i], int) and i < 3:
                try:
                    temp = str(MATRIX[y][x-i]) + temp
                    MATRIX[y][x-i] = "."
                    i += 1
                except IndexError:
                    break
        except IndexError:
            print("hello")
        try:
            while isinstance(MATRIX[y][x+j], int) and j < 3:
                try:
                    temp = temp + str(MATRIX[y][x+j])
                    MATRIX[y][x+j] = "."
                    j += 1
                except IndexError:
                    break
            MATRIX[y][x] = '.'

        except IndexError:
            print("hello")
        return int(temp)
    else:
        return 0


def day3():
    total = 0
    blub = 0
    with open('puzzle_input.txt', 'r') as file:
        for i, line in enumerate(file):
            # add nested array
            sub_matrix = []
            for s, char in enumerate(line):
                if char != "\n":
                    if char in SYMBOLS or char == '.':
                        sub_matrix.append(char)
                    else:
                        sub_matrix.append(int(char))
                s += 1
            MATRIX.append(sub_matrix)
        i += 1
    for y, row in enumerate(MATRIX):
        for x, value in enumerate(row):
            # if value in SYMBOLS:
            #     # print(value)
            #     temp = part1(y, x)
            #     if isinstance(temp, int):
            #         total += temp
            if value == '*':

                p2 = part2(y, x)
                if isinstance(p2, int):
                    blub += p2
            x += 1
        y += 1
    print(total)
    print(blub)


day3()
