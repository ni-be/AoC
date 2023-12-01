# AoC2023 day 1

# read txt line by line
# extract first and last number of string
# if there is only 1 number i.e. 7 it will equal 77
# sum the numbers for each line

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# total = 0
# with open('puzzle_input.txt', 'r') as file:
#     for line in file:
#         x = []
#         for char in line:
#             if char in numbers:
#                 if len(x) < 2:
#                     x.append(char)
#                 else:
#                     x[1] = char
#         if len(x) > 1:
#             line_sum = x[0] + x[1]
#         else:
#             line_sum = x[0] + x[0]
#         total += int(line_sum)
# print(total)

# clean up version


def calibration_values(input):
    sum = 0
    with open(input, 'r') as file:
        for line in file:
            line_values = char_ext(line)
            line_sum = summarizer(line_values)
            sum += int(line_sum)
    print(sum)


def char_ext(line):
    line_values = []
    for char in line:
        if char in NUMBERS:
            if len(line_values) < 2:
                line_values.append(char)
            else:
                line_values[1] = char
    return line_values


def summarizer(line_values):
    if len(line_values) > 1:
        line_sum = line_values[0] + line_values[1]
    else:
        line_sum = line_values[0] + line_values[0]
    return line_sum


calibration_values('puzzle_input.txt')
