import re


class reader:
    def __init__(self):
        self.input = []
        self.stack_data = []
        self.instructions = []
        self.stacks = []
        self.reg = re.compile(r"\d+")

    def read_input(self):
        with open("input.in", "r") as f:
            self.input = f.read().splitlines()
        self.separate_input_data()
        self.initialize_stacks()
        self.populate_stacks()

    def separate_input_data(self):
        for i, line in enumerate(self.input):
            if line == "":
                self.stack_data = self.input[:i]
                self.instructions = self.input[i + 1:]
                return

    def initialize_stacks(self):
        stacks = self.stack_data.pop().split()
        for num in stacks:
            self.stacks.append(stack(int(num)))

    def execute_instructions(self):
        tmp_number = -1
        for instruction in self.instructions:
            tmp = stack(tmp_number)
            nums = self.reg.findall(instruction)
            n = int(nums[0])
            from_index = int(nums[1]) - 1
            to_index = int(nums[2]) - 1
            for _ in range(n):
                item = self.stacks[from_index].remove()
                tmp.add(item)

            for _ in range(n):
                item = tmp.remove()
                self.stacks[to_index].add(item)

    def print_remaining(self):
        remaining = ""
        for stack in self.stacks:
            remaining = remaining + stack.remove()
        print(remaining)

    def populate_stacks(self):
        for stack in self.stacks:
            self.populate_stack(stack)

    def populate_stack(self, stack):
        number = stack.number
        index = number + 3 * (number - 1)
        for l in reversed(self.stack_data):
            c = l[index]
            if c != " ":
                stack.add(c)

    def print_stacks(self):
        for stack in self.stacks:
            print(stack)

    def write(self):
        for line in self.stack_data:
            print(line)
        for line in self.instructions:
            print(line)


class stack:
    def __init__(self, number):
        self.number = number
        self.contents = []

    def add(self, item):
        self.contents.append(item)

    def remove(self):
        return self.contents.pop()

    def __str__(self):
        return str(self.number) + ": " + " ".join(self.contents)


def main():
    r = reader()
    r.read_input()
    r.execute_instructions()
    r.print_remaining()


if __name__ == "__main__":
    main()
