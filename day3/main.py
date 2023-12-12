from sys import stdin
from typing import List
from string import ascii_lowercase, ascii_uppercase


def get_input():
    return [line.strip() for line in stdin]


def prio(c: str):
    if c.isupper():
        return ascii_uppercase.index(c) + 27
    return ascii_lowercase.index(c) + 1


def intersection(*lists: List):
    sets = [set(l) for l in lists]
    inter = set.intersection(*sets)
    return next(iter(inter))


def middle_split(s: str):
    l = len(s) // 2
    lhs, rhs = s[:l], s[l:]
    return lhs, rhs


def part_one(lines: List[str]):
    parts = [middle_split(line) for line in lines]
    common = [intersection(l, r) for l, r in parts]
    prios = [prio(c) for c in common]
    return sum(prios)


def get_triplets(ls: List):
    return list(zip(*[iter(ls)] * 3))


def part_two(lines: List[str]):
    triplets = get_triplets(lines)
    common = [intersection(a, b, c) for a, b, c in triplets]
    prios = [prio(c) for c in common]
    return sum(prios)


def main():
    lines = get_input()
    part_one_res = part_one(lines)
    part_two_res = part_two(lines)
    print(f"Part one: {part_one_res:}")
    print(f"Part two: {part_two_res:}")


if __name__ == "__main__":
    main()
