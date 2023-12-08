import linecache


def counter(content, option):
    count = 0
    temp = []
    for entry in (content.split('|')[1]).split():
        if entry.isnumeric():
            temp.append(int(entry))
    for winners in (content.split('|')[0]).split(' '):
        if winners.isdigit():
            if int(winners) in temp:
                if count < 1 or option == 2:
                    count += 1
                elif count > 0 and option == 1:
                    count += count
    return count


def part1(input):
    lines = linecache.getlines(input)
    result = 0
    for i, ln in enumerate(lines):
        content = ln.split(':')[1]
        count = counter(content, 1)
        result += count
    print(result)


def part2(input):
    lines = linecache.getlines(input)
    game = []
    cards = []
    for i, ln in enumerate(lines):
        content = ln.split(':')[1]
        game.append(counter(content, 2))
        cards.append(1)
    for j, win in enumerate(game):
        for z in range(cards[j]):
            for x in range(int(win)):
                if cards[j+x+1] in cards:
                    cards[j+x+1] = cards[j+x+1] + 1
    print(sum(cards))

    # part1('input.txt')
part2('puzzle_input.txt')
