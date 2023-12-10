from linecache import getlines


moves = {
    ('|', (1, 0)): (1, 0),
    ('|', (-1, 0)): (-1, 0),
    ('-', (0, 1)): (0, 1),
    ('-', (0, -1)): (0, -1),
    ('L', (1, 0)): (0, 1),
    ('L', (0, -1)): (-1, 0),
    ('J', (1, 0)): (0, -1),
    ('J', (0, 1)): (-1, 0),
    ('7', (-1, 0)): (0, -1),
    ('7', (0, 1)): (1, 0),
    ('F', (-1, 0)): (0, 1),
    ('F', (0, -1)): (1, 0),
}


def part2(path):
    def area2(cords):
        A = 0
        for i in range(len(cords)):
            A += (cords[i-1][0] + cords[i][0]) * (cords[i-1][1] - cords[i][1])
        return abs(A)

    a2 = area2(path)
    ans = (a2 - len(path) + 2)//2
    return ans + 1


def part1(game, start):
    count = 1
    if start[1] > 10:
        move = (0, -1)
    else:
        move = (0, 1)

    location = (start[0] + move[0], start[1]+move[1])
    history = [start, location]
    while location != start:
        move = moves[(game[location[0]][location[1]], move)]
        location = (location[0]+move[0], location[1] + move[1])
        history.append(location)

        count += 1
    print(count//2)
    print(part2(history))


def find_start(game):
    for y, row in enumerate(game):
        for x, char in enumerate(row):
            if char == 'S':
                return (y, x)


def solve(input):
    lines = getlines(input)

    game = [[char.strip() for char in line.strip()] for line in lines]
    start = find_start(game)
    # print(game)
    part1(game, start)


solve("d10_puzzle.txt")
