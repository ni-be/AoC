# Day 03 Advent of Code 2024

input = "d04.txt"

data = [list(l) for l in open(input).read().splitlines()]


def part1(data):
    inverted = list(zip(*data))
    diag = [[] for _ in range(len(data) + len(data[0]) - 1)]
    antidiag = [[] for _ in range(len(diag))]

    min_bdiag = -len(data) + 1
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            diag[x + y].append(val)
            antidiag[x - y - min_bdiag].append(val)

    count = 0
    for matrice in [data, inverted, diag, antidiag]:
        for line in matrice:
            line = "".join(line)
            count += line.count("XMAS") + line.count("SAMX")

    return count


def part2(data):
    count = 0
    for i, line in enumerate(data[1:-1], start=1):
        for j, val in enumerate(line[1:-1], start=1):
            if val != "A":
                continue
            valid = ["MSMS", "SMSM", "SMMS", "MSSM"]
            if (
                data[i - 1][j - 1]
                + data[i + 1][j + 1]
                + data[i + 1][j - 1]
                + data[i - 1][j + 1]
                in valid
            ):
                count += 1

    return count


print(part1(data), part2(data))
