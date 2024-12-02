# Day 02 Advent of Code 2024
import bisect

file_path = "d02.txt"


temp = 0


def valid(val):
    inc = all(1 <= (val[i + 1] - val[i]) <= 3 for i in range(len(val) - 1))
    dec = all(1 <= (val[i] - val[i + 1]) <= 3 for i in range(len(val) - 1))
    if inc or dec:
        return True


with open(file_path, "r") as file:
    for line in file:
        val = list(map(int, line.split()))
        if valid(val):
            temp += 1
        else:
            for i in range(len(val)):
                mod = val[:i] + val[i + 1 :]
                if valid(mod):
                    temp += 1
                    break
print(temp)
