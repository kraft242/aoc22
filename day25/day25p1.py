from math import log


class Reader:
    def __init__(self):
        self.input = []
        self.base = 5

    def read(self):
        file_name = "example.in"
        with open(file_name, "r") as f:
            self.input = f.read().splitlines()

    def run(self):
        res = []
        for snafu in self.input:
            dec = self.__snafu_to_dec(snafu)
            res.append(dec)

        for d in res:
            print(d)

    def __log_five(self, a):
        return log(a, self.base)

    def __snafu_to_dec(self, snafu):
        dec = 0
        l = len(snafu) - 1
        for i, c in enumerate(snafu):
            exp = l - i
            val = self.__get_snafu_digit_value(c)
            tmp = val * (self.base ** exp)
            dec += tmp
        return dec

    def __get_snafu_digit_value(self, digit):
        if digit == "1":
            return 1
        elif digit == "2":
            return 2
        elif digit == "-":
            return -1
        elif digit == "0":
            return 0
        return -2

    def __dec_to_snafu(self, dec):
        snafu = []
        q = dec
        dec_str = str(dec)
        while q != 0:
            q = self.__calc_quotient(q)
            r = self.__calc_remainder(q)
            snafu.append(r)

    def __calc_quotient(self, dec):
        return dec // self.base

    def __calc_remainder(self, dec):
        r = dec % self.base
        if r == 3:
            return "1="
        elif r == 4:
            return "1-"
        return str(r)


def main():
    reader = Reader()
    reader.read()
    reader.run()


if __name__ == "__main__":
    main()
