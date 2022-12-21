class Reader:
    def __init__(self):
        self.input = []
        self.monkeys = {}

    def read(self):
        file_name = "example.in"
        with open(file_name, "r") as f:
            inp = f.read().splitlines()
            self.__init_monkeys(inp)
            self.__add_monkey_jobs(inp)

    def __init_monkeys(self, inp):
        for line in inp:
            name = line.split()[0].strip(":")
            self.monkeys[name] = Monkey()

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

    def run(self):
        root = self.monkeys["root"]
        return root.get_value()


class Monkey:
    def __init__(self):
        self.left = None
        self.op = None
        self.right = None
        self.val = None

    def get_value(self):
        if self.val != None:
            return self.val
        # Addition
        if self.op == "+":
            return self.left.get_value() + self.right.get_value()
        # Subtraction
        elif self.op == "-":
            return self.left.get_value() - self.right.get_value()
        # (Integer) Division
        elif self.op == "/":
            return self.left.get_value() // self.right.get_value()
        # Multiplication
        return self.left.get_value() * self.right.get_value()


class Tree:
    pass


def main():
    reader = Reader()
    reader.read()
    res = reader.run()
    print(res)


if __name__ == "__main__":
    main()
