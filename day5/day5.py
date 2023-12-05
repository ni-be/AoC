def seed_runner(input):
    return [(n, 1) for n in input]


def seed_runner2(input):
    return list(zip(input[::2], input[1::2]))


def solver(groups, seeds):
    ranges = []
    for g in groups[1:]:
        step_mapping = [tuple(map(int, l.split())) for l in g.splitlines()[1:]]
        temp = []

        new_ranges = []

        for start, r_len in seeds:
            while r_len != 0:
                found_match = False
                best_dist = r_len

                for dst, src, length in step_mapping:
                    if src <= start < src+length:
                        # Found a match
                        off = start - src
                        rem_length = min(length - off, r_len)
                        new_ranges.append((dst+off, rem_length))
                        start += rem_length
                        r_len -= rem_length
                        found_match = True
                        break
                    else:
                        if start < src:
                            best_dist = min(src - start, best_dist)

                if not found_match:
                    handling_len = min(best_dist, r_len)
                    new_ranges.append((start, handling_len))
                    start += handling_len
                    r_len -= handling_len

        seeds = new_ranges
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


def solve(s, seed_interpreter):
    groups = s.split('\n\n')
    seed_ranges = seed_runner(list(map(int, groups[0].split()[1:])))
    for g in groups[1:]:
        step_mapping = [tuple(map(int, l.split()))
                        for l in g.splitlines()[1:]]
        # print(step_mapping)
        new_ranges = []

        for start, r_len in seed_ranges:
            while r_len != 0:
                found_match = False
                best_dist = r_len

                for dst, src, length in step_mapping:
                    if src <= start < src+length:
                        # Found a match
                        off = start - src
                        rem_length = min(length - off, r_len)
                        new_ranges.append((dst+off, rem_length))
                        start += rem_length
                        r_len -= rem_length
                        found_match = True
                        break
                    else:
                        if start < src:
                            best_dist = min(src - start, best_dist)

                if not found_match:
                    handling_len = min(best_dist, r_len)
                    new_ranges.append((start, handling_len))
                    start += handling_len
                    r_len -= handling_len

        # print(new_ranges)
        seed_ranges = new_ranges

    return min(start for start, length in seed_ranges)


def part1_check(s):
    def seed_interpreter(nums):
        return [(n, 1) for n in nums]

    answer = solve(s, seed_interpreter)

    print(answer)


# print(data)
# part1(data)
part1(data)
part1_check(data)
