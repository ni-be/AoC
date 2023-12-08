def seed_runner(input):
    return [(n, 1) for n in input]


def seed_runner2(input):
    return list(zip(input[::2], input[1::2]))


def solver(groups, seeds):
    for g in groups[1:]:
        step_mapping = [tuple(map(int, l.split())) for l in g.splitlines()[1:]]
        temp = []

        for start, r_len in seeds:
            while r_len != 0:
                found_match = False
                best_dist = r_len

                for dst, src, length in step_mapping:
                    if src <= start < src+length:
                        # Found a match
                        off = start - src
                        rem_length = min(length - off, r_len)
                        temp.append((dst+off, rem_length))
                        start += rem_length
                        r_len -= rem_length
                        found_match = True
                        break
                    else:
                        if start < src:
                            best_dist = min(src - start, best_dist)

                if not found_match:
                    handling_len = min(best_dist, r_len)
                    temp.append((start, handling_len))
                    start += handling_len
                    r_len -= handling_len

        seeds = temp
    return min(start for start, length in seeds)


def part1(data):
    groups = data.split('\n\n')
    seeds = seed_runner(list(map(int, groups[0].split()[1:])))
    result = solver(groups, seeds)
    print(result)


def part2(data):
    groups = data.split('\n\n')
    seeds = seed_runner2(list(map(int, groups[0].split()[1:])))
    result = solver(groups, seeds)
    print(result)


with open("puzzle_input.txt") as f:
    data = f.read().strip()

part1(data)
