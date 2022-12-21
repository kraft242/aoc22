from sympy import symbols, Eq, solve


class Reader:
    def __init__(self):
        self.input = []
        self.monkeys = {}

    def read(self):
        file_name = "input.in"
        with open(file_name, "r") as f:
            inp = f.read().splitlines()
            self.__init_monkeys(inp)
            self.__add_monkey_jobs(inp)

    def __init_monkeys(self, inp):
        for line in inp:
            name = line.split()[0].strip(":")
            self.monkeys[name] = Monkey(name)

    def __add_monkey_jobs(self, inp):
        for line in inp:
            line = line.split()
            name = line[0].strip(":")
            monkey = self.monkeys[name]
            # Number
            if len(line) == 2:
                monkey.val = int(line[1])
            # Expression
            else:
                monkey.left = self.monkeys[line[1]]
                monkey.op = line[2]
                monkey.right = self.monkeys[line[3]]

    def __str__(self):
        root = self.monkeys["root"]
        return str(root)

    def run(self):
        root = self.monkeys["root"]
        eq = str(root)
        x = symbols("x")
        sol = solve(eq, x)
        return sol[0]


class Monkey:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.op = None
        self.right = None
        self.val = None

    def __str__(self):
        if self.name == "root":
            return "(" + str(self.left) + " - " + str(self.right) + ")"
        if self.name == "humn":
            return "x"
        if self.val != None:
            return str(self.val)
        return "(" + str(self.left) + " " + self.op + " " + str(self.right) + ")"


class Tree:
    pass


def main():
    reader = Reader()
    reader.read()
    res = reader.run()
    print(res)


if __name__ == "__main__":
    main()
