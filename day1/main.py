from sys import stdin
from typing import List


def get_input():
    lines = [line for line in stdin]
    elves = "".join(lines).split("\n\n")
    return [elf.replace("\n", " ") for elf in elves]


def to_int_lists(lines: List[str]):
    return [[int(n) for n in line.split()] for line in lines]


def part_one(lines: List[str]):
    elves = to_int_lists(lines)
    elves.sort(key=sum)
    return sum(elves[-1])


def part_two(lines: List[str]):
    elves = to_int_lists(lines)
    elves.sort(key=sum)
    top_three = elves[-3:]
    return sum(sum(elf) for elf in top_three)


def main():
    lines = get_input()
    part_one_res = part_one(lines)
    part_two_res = part_two(lines)
    print(f"Part one: {part_one_res:}")
    print(f"Part two: {part_two_res:}")


if __name__ == "__main__":
    main()
