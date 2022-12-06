def split_input(s):
    l = s.split(",")
    return l[0], l[1]

def get_list(r):
    tmp = r.split("-")
    start = int(tmp[0])
    end = int(tmp[1]) + 1
    return [i for i in range(start,end)]


def overlap(one, two):
    l_one = get_list(one)
    l_two = get_list(two)
    for i in l_one:
        for j in l_two:
            if i == j:
                return True
    return False



sum = 0
inp = open("input", "r")
for line in inp:
    one, two = split_input(line)
    if overlap(one, two):
        sum += 1

print(sum)
