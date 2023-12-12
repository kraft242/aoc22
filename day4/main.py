from sys import stdin
from typing import List, Tuple


def get_input():
    return [line.strip() for line in stdin]


def get_pairs(line: str):
    lhs, rhs = line.split(",")
    return get_tuples(lhs, rhs)


def get_tuples(lhs: str, rhs: str):
    la, lb = lhs.split("-")
    ra, rb = rhs.split("-")
    return (int(la), int(lb)), (int(ra), int(rb))


def pair_contains(l: Tuple[int, int], r: Tuple[int, int]):
    l_start, l_end = l
    r_start, r_end = r
    r_in_l = l_start <= r_start and r_end <= l_end
    l_in_r = r_start <= l_start and l_end <= r_end
    return r_in_l or l_in_r


def part_one(lines: List[str]):
    pairs = [get_pairs(line) for line in lines]
    return sum(pair_contains(l, r) for l, r in pairs)


def pairs_overlap(l: Tuple[int, int], r: Tuple[int, int]):
    l_start, l_end = l
    r_start, r_end = r
    r_gt_l = l_start <= r_start <= l_end
    l_gt_r = r_start <= l_start <= r_end
    return r_gt_l or l_gt_r


def part_two(lines: List[str]):
    pairs = [get_pairs(line) for line in lines]
    return sum(pairs_overlap(l, r) for l, r in pairs)


def main():
    lines = get_input()
    part_one_res = part_one(lines)
    part_two_res = part_two(lines)
    print(f"Part one: {part_one_res:}")
    print(f"Part two: {part_two_res:}")


if __name__ == "__main__":
    main()
