def split_input(s):
    l = s.split(",")
    return l[0], l[1]


def get_tuple(r):
    tmp = r.split("-")
    start = int(tmp[0])
    end = int(tmp[1])
    return (start, end)


def contained(one, two):
    one_start = one[0]
    one_end = one[1]
    two_start = two[0]
    two_end = two[1]
    one_contains_two = one_start <= two_start and one_end >= two_end
    two_contains_one = two_start <= one_start and two_end >= one_end
    return one_contains_two or two_contains_one


sum = 0
inp = open("input", "r")
for line in inp:
    one, two = split_input(line)
    l_one = get_tuple(one)
    l_two = get_tuple(two)
    if contained(l_one, l_two):
        sum += 1

print(sum)
