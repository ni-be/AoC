import sys
import functools


@functools.cache
def calc(record, groups):
    if not groups:
        if "#" not in record:
            return 1
        else:
            return 0
    if not record:
        return 0

    next_character = record[0]
    next_group = groups[0]

    def pound():
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")
        if this_group != next_group * "#":
            return 0
        if len(record) == next_group:
            if len(groups) == 1:
                return 1
            else:
                return 0
        if record[next_group] in "?.":
            return calc(record[next_group+1:], groups[1:])
        return 0

    def dot():
        return calc(record[1:], groups)

    if next_character == '#':
        out = pound()

    elif next_character == '.':
        out = dot()

    elif next_character == '?':
        out = dot() + pound()

    else:
        raise RuntimeError
    return out


with open(sys.argv[1]) as file:
    raw = file.read()
raw_file = raw.strip()

output = 0
for entry in raw_file.split("\n"):
    record, raw_groups = entry.split()
    group = [int(i) for i in raw_groups.split(',')]
    group2 = group + group*4
    rec = f"?{record}"
    record2 = record + rec*4
    # output += calc(record, tuple(group))
    output += calc(record2, tuple(group2))

print(output)
