import sys
import functools


# def vertical_reflection(columns):
#     ans = ans2 = 0
#     for i in range(len(columns) - 1):
#         cc = 0
#         low = i
#         high = i + 1
#         while 0 <= low and high < len(columns):
#             diff = columns[low] ^ columns[high]
#             if diff.bit_count() == 1:
#                 cc += 1
#             elif diff.bit_count() > 1:
#                 cc += 2
#             low -= 1
#             high += 1
#         if cc == 0:
#             ans += i + 1
#         elif cc == 1:
#             ans2 += i + 1
#     return ans, ans2


# @functools.cache
# def horizontal_reflection(row):
#     ans1 = ans2 = 0
#     # print(row)
#     for i in range(len(row)-1):
#         cc = 0
#         low = i
#         high = i+1

#         while 0 <= low and high < len(rows):
#             try:
#                 difference = row[low] ^ row[high]
#                 if difference.bit_count() == 1:
#                     cc += 1
#                 elif difference.bit_count() > 1:
#                     cc += 2
#                 low -= 1
#                 high += 1
#             except IndexError:
#                 continue
#         if cc == 0:
#             ans1 = (i+1)*100
#         elif cc == 1:
#             ans2 = (i+1)*100
#     return ans1, ans2


# def solve(columns, rows):
#     answer1 = 0
#     answer2 = 0
#     for row in rows:
#         # print(row)
#         ans, ans2 = horizontal_reflection(tuple(row))
#         answer1 += ans
#         answer2 += ans2
#     for cols in columns:
#         cans, cans2 = vertical_reflection(cols)
#         answer1 += cans
#         answer2 += cans2

#     print("ANS1 >>> ", answer1)
# #     print("ANS2 >>> ", answer2)


# def data_prep(input):
#     column = []
#     rows = []
#     for data in input:
#         lines = data.splitlines(False)

#         row = [0] * len(lines)
#         cols = [0] * len(lines[0])
#         for y, line in enumerate(lines):
#             for x, c in enumerate(line):
#                 if c == "#":
#                     row[y] += 1 << x + 1
#                     cols[x] += 1 << y + 1
#         column.append(cols)
#         rows.append(row)
#     return column, rows


# with open(sys.argv[1]) as file:
#     # game = file.read().split("\n\n")
# #   # columns, rows = data_prep(game)
# #   # solve(columns, rows)
# # print(raw_file)c

game = list(map(str.split, open(sys.argv[1]).read().split('\n\n')))


def solve(ds):
    for i in range(len(ds)):
        if sum(c != d for l, m in zip(ds[i-1::-1], ds[i:])
               for c, d in zip(l, m)) == s:
            return i
    else:
        return 0


for s in 0, 1:
    print(sum(100 * solve(ds) + solve([*zip(*ds)]) for ds in game))
