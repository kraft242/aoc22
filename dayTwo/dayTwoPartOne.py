def result(opp, me):
    if opp == "A":
        if me == "X":
            return 3
        if me == "Y":
            return 6
        else:
            return 0
    elif opp == "B":
        if me == "X":
            return 0
        if me == "Y":
            return 3
        else:
            return 6
    else:
        if me == "X":
            return 6
        if me == "Y":
            return 0
        else:
            return 3


choice = {"X": 1, "Y": 2, "Z": 3}
total_score = 0

inp = open("input","r")
for line in inp:
    play = line.strip().split(" ")
    opp = play[0]
    me = play[1]
    score = result(opp, me) + choice.get(me)
    total_score += score
inp.close()
print(total_score)