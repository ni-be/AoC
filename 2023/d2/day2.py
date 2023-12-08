# Day 2 Cube Conundrum

COLORS = [12, 13, 14]


def day2():
    id_sum = 0
    failed_game = []
    part_two = []
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            game = int(game_id(line))
            set = find_sets(line)
            # print(set)
            for draw in set:
                result = draw_split(draw)
                for balls in result:
                    game_draw = [game, 0, 0, 0]
                    ball_split = number_balls(balls)
                    # print(ball_split)
                    if ball_split[0] == "red":
                        game_draw[1] = ball_split[1]
                    elif ball_split[0] == "green":
                        game_draw[2] = ball_split[1]
                    elif ball_split[0] == "blue":
                        game_draw[3] = ball_split[1]
                    part_two.append(game_draw)
                    failed_id = filter_games(game_draw)
                    if failed_id not in failed_game:
                        failed_game.append(failed_id)
            if game not in failed_game:
                id_sum += game
    print(id_sum)
    # add part2
    day2_two(part_two)


def day2_two(data):
    store = []
    sub = [0, 0, 0, 0]
    for draws in data:
        if sub[0] != draws[0] and sub[0] != 0:
            store.append(sub)
            sub = [0, 0, 0, 0]

        for i in range(4):
            if sub[i] <= draws[i]:
                sub[i] = draws[i]
    store.append(sub)

    sum = 0
    for game in store:
        sum += game[1]*game[2]*game[3]
    print(sum)


def filter_games(game):
    if game[1] > COLORS[0] or game[2] > COLORS[1] or game[3] > COLORS[2]:
        id = game[0]
        return id


def number_balls(balls):
    ball_split = ['0', '0']
    string = ''
    number = ''
    for char in balls:
        if not char.isdigit() and not char.isspace():
            string += char
        elif not char.isspace() and not char.isalpha():
            number += char
    ball_split[0] = string
    ball_split[1] = int(number)
    return ball_split


def draw_split(draw):
    draw_split = []
    for i in range(3):
        try:
            draw_split.append(draw.split(",")[i])
        except IndexError:
            continue
    return draw_split


def find_sets(line):
    contents = line.split(":")[1]
    set = []
    for i in range(10):
        try:
            set.append(contents.split(";")[i])
        except IndexError:
            continue

    set2 = [item.strip("\n") for item in set]
    return set2


def game_id(line):
    gid = ''
    id = line.split(":")[0]
    for char in id:
        if char.isdigit():
            gid += char
    return gid


day2()
