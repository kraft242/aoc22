class Driver:
    def __init__(self):
        self.input = []
        self.device = None

    def read(self):
        file_name = "input.in"
        with open(file_name, "r") as f:
            self.input = f.read().splitlines()
        self.device = Device(self.input)

    def run(self):
        self.device.execute_instructions()

    def get_result(self):
        return self.device.get_result()


class Device:
    def __init__(self, instructions):
        self.instructions = instructions
        self.register = 1
        self.duration = {"noop": 1, "addx": 2}
        self.clock_cycle = 0
        self.signal_strengths = []
        self.width = 40
        self.height = 6
        self.screen = ["." for _ in range(self.width*self.height)]

    def __cycle_is_multiple_of_40(self):
        return self.clock_cycle != 0 and (self.clock_cycle - int(self.width / 2)) % self.width == 0

    def __cycle_is_20(self):
        return self.clock_cycle == int(self.width / 2)

    def __cycle_is_target(self):
        return self.__cycle_is_20() or self.__cycle_is_multiple_of_40()

    def __instruction_is_noop(self, instruction):
        return len(instruction) == 1

    def __instruction_is_addx(self, instruction):
        return len(instruction) == 2

    def __increment_clock(self):
        self.clock_cycle += 1

    def __update_screen(self):
        i = self.clock_cycle
        if self.__sprite_contains_current_pixel():
            c = "#"
            self.screen[i] = c
        self.__increment_clock()

    def __sprite_contains_current_pixel(self):
        sprite_start_index = self.register - 1
        sprite_end_index = self.register + 1
        pixel_index = (self.clock_cycle) % self.width
        return pixel_index >= sprite_start_index and pixel_index <= sprite_end_index

    def __increment_register(self, val):
        self.register += val

    def __print_start_cycle_debug(self, instruction):
        cycle_num = self.clock_cycle + 1
        s = "Start cycle \t" + str(cycle_num) + \
            ": begin executing " + " ".join(instruction)
        print(s)

    def __print_during_cycle_debug(self):
        cycle_num = self.clock_cycle
        pos = cycle_num - 1
        s = "During cycle \t" + \
            str(cycle_num) + ": CRT draws pixel in position " + str(pos) + "\n"
        print(s)

    def __execute_instruction(self, instruction):
        instruction_type = instruction[0]
        self.__print_start_cycle_debug(instruction)
        num_steps = self.duration.get(instruction_type)
        for _ in range(num_steps):
            self.__update_screen()
            self.__print_during_cycle_debug()
        if self.__instruction_is_addx(instruction):
            val = int(instruction[1])
            self.__increment_register(val)

    def __index_is_breakpoint(self, i):
        breakpoint = self.width
        return i != 0 and i % breakpoint == 0

    def get_result(self):
        res = ""
        screen_str = self.screen
        for i, c in enumerate(screen_str):
            if self.__index_is_breakpoint(i):
                res += "\n"
            res += c
        return res

    def execute_instructions(self):
        for instruction in self.instructions:
            instruction = instruction.split()
            self.__execute_instruction(instruction)


def main():
    driver = Driver()
    driver.read()
    driver.run()
    res = driver.get_result()
    print(res)


if __name__ == "__main__":
    main()
