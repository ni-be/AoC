# Day 01 Advent of Code 2024
import bisect

file_path = "d01.txt"

lnum = []
rnum = []

with open(file_path, "r") as file:
    for line in file:
        l, r = map(int, line.split())
        bisect.insort(lnum, l)
        bisect.insort(rnum, r)

d = 0
for l, r in zip(lnum, rnum):
    d += abs(l - r)

print(d)

occurs = 0

for l in lnum:
    s = rnum.count(l)
    occurs += s * l
print(occurs)
