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
        signal_strengths = self.device.signal_strengths
        signal_strength = sum(signal_strengths)
        return signal_strength

class Device:
    def __init__(self, instructions):
        self.instructions = instructions
        self.register = 1
        self.duration = {"noop": 1, "addx": 2}
        self.clock_cycle = 0
        self.signal_strengths = []

    def __cycle_is_multiple_of_40(self):
        return self.clock_cycle != 0 and (self.clock_cycle - 20) % 40 == 0

    def __cycle_is_20(self):
        return self.clock_cycle == 20

    def cycle_is_target(self):
        return self.__cycle_is_20() or self.__cycle_is_multiple_of_40()

    def instruction_is_noop(self, instruction):
        return len(instruction) == 1

    def instruction_is_addx(self,instruction):
        return len(instruction) == 2

    def increment_clock(self):
        self.clock_cycle += 1

    def increment_register(self, val):
        self.register += val

    def calculate_signal_strength(self):
        val = self.clock_cycle * self.register
        self.signal_strengths.append(val)

    def execute_instruction(self, instruction):
        instruction_type = instruction[0]
        num_steps = self.duration.get(instruction_type)
        for _ in range(num_steps):
            self.increment_clock()
            if self.cycle_is_target():
                self.calculate_signal_strength()
        if self.instruction_is_addx(instruction):
            val = int(instruction[1])
            self.increment_register(val)


    def execute_instructions(self):
        for instruction in self.instructions:
            instruction = instruction.split()
            self.execute_instruction(instruction)
        

def main():
    driver = Driver()
    driver.read()
    driver.run()
    res = driver.get_result()
    print(res)


if __name__ == "__main__":
    main()