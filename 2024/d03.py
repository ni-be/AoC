# Day 03 Advent of Code 2024
import re


def get_input(filepath):
    with open(filepath, "r") as file:
        return file.read()


def add(a, b):
    return a + b


def format_input(input_str):
    return input_str.strip().split("\n")


MUL_PATTERN = r"mul\(\d{1,3},\d{1,3}\)"


def sum_muls(muls):
    total = 0
    for match in muls:
        x, y = match.replace("mul(", "").replace(")", "").split(",")
        total += int(x) * int(y)
    return total


def solution1(input_str):
    lines = format_input(input_str)
    matches = [
        match.group(0) for line in lines for match in re.finditer(MUL_PATTERN, line)
    ]
    return sum_muls(matches)


MUL_DO_DONT_PATTERN = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"


def solution2(input_str):
    lines = format_input(input_str)
    matches = [
        match.group(0)
        for line in lines
        for match in re.finditer(MUL_DO_DONT_PATTERN, line)
    ]

    kept = []
    keeping = True
    for match in matches:
        if match == "do()":
            keeping = True
            continue
        if match == "don't()":
            keeping = False
            continue
        if keeping:
            kept.append(match)

    return sum_muls(kept)


prog = get_input("d03.txt")
print(solution1(prog))
print(solution2(prog))
