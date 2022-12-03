class rucksack:
    def __init__(self,s):
        l = int(len(s)/2)
        self.s_one = s[0:l]
        self.s_two = s[l:]
        self.s = s

    def get_duplicate(self):
        for c in self.s_one:
            for d in self.s_two:
                if c == d:
                    return c
        return ""

priority = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52}

inp = open("input","r")
sum = 0
for line in inp:
    r = rucksack(line)
    duplicate = r.get_duplicate()
    sum += priority.get(duplicate)

print(sum)
    

