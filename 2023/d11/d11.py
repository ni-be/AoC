from linecache import getlines


def manhatten(input):
    lines = getlines(input)
    data = [[char.strip() for char in line.strip()] for line in lines]
    rows = []
    cols = []
    galaxies = []
    result = [0, 0]
    expansion_key = [1, 999999]

    for y, row in enumerate(data):
        if '#' not in row:
            rows.append(y)
            continue
        for x, c in enumerate(row):
            if c == '#':
                galaxies.append((x, y))

    for x, _ in enumerate(data[0]):
        if '#' not in [row[x] for _, row in enumerate(data)]:
            cols.append(x)

    for g, galaxy in enumerate(galaxies):
        for n in range(g + 1, len(galaxies)):

            y = (min(galaxies[n][0], galaxy[0]),
                 max(galaxies[n][0], galaxy[0]))
            x = (min(galaxies[n][1], galaxy[1]),
                 max(galaxies[n][1], galaxy[1]))

            for i, key in enumerate(expansion_key):
                result[i] = result[i] + y[1] - y[0] + x[1] - x[0]
                result[i] = result[i] + \
                    sum(key for e in cols if e in range(y[0], y[1]))
                result[i] = result[i] + \
                    sum(key for e in rows if e in range(x[0], x[1]))
    print(result)


manhatten('puzzle_input')
