import sys

class Elf:
    def __init__(self, items):
        self.items = items
        self.sum = sum(items)

class Reader:
    def __init__(self, _input):
        self.input = _input
        self.elves = []

    def read(self):
        items = []
        for line in self.input:
            if line == "\n":
                elf = Elf(items)
                self.elves.append(elf)
                items = []
            else:
                items.append(int(line.strip("\n")))
        elf = Elf(items)
        self.elves.append(elf)

    def find_largest(self):
        largest = 0
        for elf in self.elves:
            if elf.sum > largest:
                e = elf
                largest = elf.sum
        self.elves.remove(e)
        return largest


def main():
    reader = Reader(sys.stdin)
    reader.read()
    first = reader.find_largest()
    second = reader.find_largest()
    third = reader.find_largest()
    print(first + second + third)

if __name__ == "__main__":
    main()
