class Reader:
    def __init__(self):
        self.input = []
        self.monkeys = {}

    def read(self):
        file_name = "input.in"
        with open(file_name, "r") as f:
            inp = f.read().splitlines()
            for line in inp:
                line = line.split()
                monkey = line[0].strip(":")
                op = line[1:]
                self.monkeys[monkey] = op

    def run(self):
        root = "root"
        return self.__run_rec(root)

    def __run_rec(self, monkey):
        job = self.monkeys[monkey]
        print(job)
        # Monkey yells number
        if len(job) == 1:
            return int(job[0])
        sub_one = job[0]
        op = job[1]
        sub_two = job[2]

        if op == "+":
            return self.__run_rec(sub_one) + self.__run_rec(sub_two)
        elif op == "-":
            return self.__run_rec(sub_one) - self.__run_rec(sub_two)
        elif op == "*":
            return self.__run_rec(sub_one) * self.__run_rec(sub_two)
        return self.__run_rec(sub_one) // self.__run_rec(sub_two)


def main():
    reader = Reader()
    reader.read()
    res = reader.run()
    print(res)


if __name__ == "__main__":
    main()
