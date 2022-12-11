import re


class Reader:
    def __init__(self):
        self.input = []
        self.monkeys = []
        self.num_reg_str = r"[0-9]+"
        self.num_reg = re.compile(self.num_reg_str)
        self.op_reg_str = r"[\+\*]"
        self.op_reg = re.compile(self.op_reg_str)
        self.num_rounds = 10000
        self.test_vals = []

    def read(self):
        file_name = "input.in"
        with open(file_name, "r") as f:
            self.input = f.read().split("\n\n")

    def init_monkeys(self):
        for line in self.input:
            lines = line.split("\n")
            self.init_monkey(lines)

        M = 1
        for p in self.test_vals:
            M *= p

        for monkey in self.monkeys:
            monkey.M = M

    def do_rounds(self):
        for i in range(self.num_rounds):
            for monkey in self.monkeys:
                res = monkey.round()
                for r in res:
                    item = r[0]
                    target = r[1]
                    self.monkeys[target].add_item(item)
            if self.is_target_round(i):
                self.print_mid_execution_num_inspections(i)
        # self.print_final_num_inspection()

    def print_final_num_inspection(self):
        s = "== After final round =="
        print(s)
        self.print_num_inspections()

    def print_mid_execution_num_inspections(self, i):
        n = i + 1
        s = "== After round " + str(n) + " =="
        print(s)
        self.print_num_inspections()

    def is_target_round(self, i):
        n = i + 1
        return n == 1 or n == 20 or n % 1000 == 0

    def get_two_most_active_monkeys(self):
        self.sort_monkeys()
        first_index = len(self.monkeys) - 1
        second_index = first_index - 1
        first_monkey = self.monkeys[first_index]
        second_monkey = self.monkeys[second_index]
        res = [first_monkey, second_monkey]
        self.print_most_active(res)
        return res

    def get_product_of_two_most_active_monkeys(self):
        res = self.get_two_most_active_monkeys()
        p = 1
        for monkey in res:
            p *= monkey.num_inspections
        self.print_level_of_monkey_business(p)
        return p

    def print_level_of_monkey_business(self, p):
        s = "The total level of monkey business is " + str(p) + "."
        print(s)

    def print_most_active(self, res):
        for monkey in res:
            monkey.print_num_inspections()

    def sort_monkeys(self):
        self.monkeys.sort()

    def print_num_inspections(self):
        for monkey in self.monkeys:
            monkey.print_num_inspections()
        print()

    def init_monkey(self, lines):
        number = int(self.num_reg.search(lines[0]).group())
        items = [int(n) for n in self.num_reg.findall(lines[1])]
        op = self.op_reg.search(lines[2]).group()
        op_val = self.num_reg.search(lines[2])
        if op_val == None:
            op_val = "item"
        else:
            op_val = int(op_val.group())
        test_val = int(self.num_reg.search(lines[3]).group())
        true_res = int(self.num_reg.search(lines[4]).group())
        false_res = int(self.num_reg.search(lines[5]).group())

        monkey = Monkey(number, items, op, op_val,
                        test_val, true_res, false_res)
        self.monkeys.append(monkey)
        self.test_vals.append(test_val)


class Monkey:
    def __init__(self, number, items, op, op_val, test_val, true_res, false_res):
        self.num_inspections = 0
        self.number = number
        self.items = items
        self.op = op
        self.op_val = op_val
        self.bored_denom = 3
        self.test_val = test_val
        self.true_res = true_res
        self.false_res = false_res
        self.DO_PRINT = False
        self.M = 0

    def __lt__(self, other):
        return self.num_inspections < other.num_inspections

    def __gt__(self, other):
        return self.num_inspections > other.num_inspections

    def add_item(self, item):
        self.items.append(item)

    def print_number(self):
        s = "Monkey " + str(self.number) + ":"
        print(s)

    def round(self):
        if self.DO_PRINT:
            self.print_number()
        thrown = []
        for item in self.items:
            self.inspect_item(item)
            item = self.calculate_worry_level(item)
            test_res = self.do_test(item)
            res = self.throw_to_other_monkey(test_res, item)
            thrown.append(res)
        self.items = []
        return thrown

    def calculate_worry_level(self, item):
        if self.op_val == "item":
            op_val = item
        else:
            op_val = self.op_val

        if self.op == "*":
            item = item * op_val
        else:
            item = item + op_val

        item = item % self.M
        if self.DO_PRINT:
            self.print_new_worry_level(item)
        return item

    def inspect_item(self, item):
        self.num_inspections += 1
        if self.DO_PRINT:
            self.print_inspect(item)

    def get_item_remainder(self, item):
        return item % self.test_val

    def print_throw(self, res):
        item = str(res[0])
        target = str(res[1])
        s = "\t\tItem with worry level " + item + \
            " is thrown to monkey " + target + "."
        print(s)

    def throw_to_other_monkey(self, test_res, item):
        res = [item]
        if test_res:
            res.append(self.true_res)
        else:
            res.append(self.false_res)
        if self.DO_PRINT:
            self.print_throw(res)
        return res

    def print_test_result(self, test_res):
        if test_res:
            s = "\t\tCurrent worry level is divisible by " + \
                str(self.test_val) + "."
        else:
            s = "\t\tCurrent worry level is not divisible by " + \
                str(self.test_val) + "."
        print(s)

    def do_test(self, item):
        res = (item % self.test_val == 0)
        if self.DO_PRINT:
            self.print_test_result(res)
        return res

    def print_bored_division_result(self, item):
        s = "\t\tMonkey gets bored with item. Worry level is divided by " + \
            str(self.bored_denom) + " to " + str(item) + "."
        print(s)

    def do_bored_division(self, item):
        item = item // self.bored_denom
        if self.DO_PRINT:
            self.print_bored_division_result(item)
        return item

    def print_new_worry_level(self, item):
        if type(self.op_val) == int:
            val = str(self.op_val)
        else:
            val = "itself"
        if self.op == "*":
            op = "multiplied"
        else:
            op = "increased"
        s = "\t\tWorry level is " + op + " by " + \
            val + " to " + str(item) + "."
        print(s)

    def print_inspect(self, item):
        s = "\tMonkey inspects an item with a worry level of " + \
            str(item) + "."
        print(s)

    def print_num_inspections(self):
        s = "Monkey " + str(self.number) + " inspected items " + \
            str(self.num_inspections) + " times."
        print(s)


def main():
    reader = Reader()
    reader.read()
    reader.init_monkeys()
    reader.do_rounds()
    reader.get_product_of_two_most_active_monkeys()


if __name__ == "__main__":
    main()
