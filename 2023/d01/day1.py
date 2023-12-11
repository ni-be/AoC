# AoC2023 day 1
import linecache
# read txt line by line
# extract first and last number of string
# if there is only 1 number i.e. 7 it will equal 77
# sum the numbers for each line

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
         'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


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


def part2(input):
    lines = linecache.getlines(input)
    # print(lines)
    result = 0
    for ln in lines:
        # print(ln)
        digits = []
        for i in range(len(ln)):
            if '0' <= ln[i] <= '9':
                digits.append(int(ln[i]))
            for k, number in WORDS.items():
                if ln[i:i+len(k)] == k:
                    digits.append(number)
        result += digits[0]*10 + digits[-1]
    print(result)


calibration_values('puzzle_input.txt')
part2('puzzle_input.txt')
