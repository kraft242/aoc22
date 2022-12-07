import re


class reader:
    def __init__(self):
        self.input = ""
        self.val = 14

    def read_input(self):
        with open("input.in", "r") as f:
            self.input = f.read().strip()

    def detect_start_of_packet_marker(self):
        l = len(self.input) - self.val - 1
        for i in range(l):
            s = self.get_fourteen(self.input, i)
            if self.no_repeating_chars(s):
                return i + self.val

    def no_repeating_chars(self, s):
        return len(set(s)) == len(s)

    def get_fourteen(self, s, start):
        end = start + self.val
        return s[start:end]


def main():
    r = reader()
    r.read_input()
    res = r.detect_start_of_packet_marker()
    print(res)


if __name__ == "__main__":
    main()
