import re


class Reader:
    def __init__(self):
        self.input = []
        num_reg_str = r"-?[0-9]+"
        self.num_reg = re.compile(num_reg_str)

    def read(self):
        file_name = "example.in"
        with open(file_name, "r") as f:
            for line in f.read().splitlines():
                nums = re.findall(self.num_reg, line)
                sensor_x = int(nums[0])
                sensor_y = int(nums[1])
                beacon_x = int(nums[2])
                beacon_y = int(nums[3])

                print(str(sensor_x) + ", " + str(sensor_y) +
                      ", " + str(beacon_x) + ", " + str(beacon_y))


class Sensor:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


class Beacon:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def main():
    reader = Reader()
    reader.read()


if __name__ == "__main__":
    main()
