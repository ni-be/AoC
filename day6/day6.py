# Day 6

def solver(data):
    result = 1
    for t, d in zip(data[0], data[1]):
        T = int(t)
        D = int(d)
        count = 0
        for i in range(1, T):
            if i*(T-i) > D:
                count += 1
        result *= count
    print(result)


def part1():
    data = []
    with open('puzzle_input.txt', 'r') as f:
        for line in f:
            ln = line.split(':')[1]
            data.append(ln.split())
    solver(data)


def part2():
    data = []
    with open('puzzle_input.txt', 'r') as f:
        for line in f:
            ln = line.split(':')[1]
            data.append((ln.replace(" ", "").split()))
    solver(data)


# part1()
part2()
