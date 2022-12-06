def result(opp, me):
    # A: Rock
    # B: Paper
    # C: Scissor
    # Lose
    if me == "X":
        if opp == "A":
            return "scissor"
        elif opp == "B":
            return "rock"
        else:
            return "paper"
    # Draw
    elif me == "Y":
        if opp == "A":
            return "rock"
        elif opp == "B":
            return "paper"
        else:
            return "scissor"
    # Win
    else:
        if opp == "A":
            return "paper"
        elif opp == "B":
            return "scissor"
        else:
            return "rock"

res = {"X": 0, "Y": 3, "Z": 6}
choice = {"rock": 1, "paper": 2, "scissor": 3}
total_score = 0


# X: Lose
# Y: Draw
# Z: Win

inp = open("input","r")
for line in inp:
    play = line.strip().split(" ")
    opp = play[0]
    me = play[1]
    score = choice.get(result(opp, me)) + res.get(me)
    total_score += score
inp.close()
print(total_score)