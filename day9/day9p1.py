from math import sqrt as sqrt


class Driver:
    def __init__(self):
        self.moves = []
        self.GRID_SIZE = 10000
        self.visited = []
        self.grid = None
        self.head = Knot()
        self.tail = Knot()

    def read(self):
        with open("input.in", "r") as f:
            for line in f.read().splitlines():
                line = line.split(" ")
                line[1] = int(line[1])
                self.moves.append(line)

    def execute_moves(self):
        for move in self.moves:
            direction = move[0]
            num_steps = move[1]
            for _ in range(num_steps):
                self.visit_current_cell()
                old_pos = self.move_head_in_direction(direction)
                if not self.tail_is_adjacent():
                    self.move_tail(old_pos)
            self.visit_current_cell()
        self.normalize_visited()

    def tail_is_adjacent(self):
        dist = int(self.distance())
        return dist < 2

    def normalize_visited(self):
        visited = []
        [visited.append(pos) for pos in self.visited if pos not in visited]
        self.visited = visited

    def visit_current_cell(self):
        self.visited.append(self.tail.pos)

    def move_tail(self, pos):
        self.tail.move_to(pos)

    def head_is(self, pos):
        return self.head.pos == pos

    def distance(self):
        tail_x = self.tail.x
        tail_y = self.tail.y
        head_x = self.head.x
        head_y = self.head.y
        dx = abs(head_x - tail_x)
        dy = abs(head_y - tail_y)
        return int(max(dx, dy))

    def move_head_in_direction(self, direction):
        curr_pos = self.head.pos
        curr_x = curr_pos[0]
        curr_y = curr_pos[1]
        # Right
        if direction == "R":
            new_pos = [curr_x + 1, curr_y]
        # Up
        elif direction == "U":
            new_pos = [curr_x, curr_y + 1]
        # Left
        elif direction == "L":
            new_pos = [curr_x - 1, curr_y]
        # Down
        else:
            new_pos = [curr_x, curr_y - 1]
        self.head.move_to(new_pos)
        return curr_pos

    def print_matrix(self):
        height = 10000
        width = 10000
        m = [["." for _ in range(width)] for _ in range(height)]
        for pos in self.visited:
            x = pos[0]
            y = pos[1]
            m[y][x] = "#"

        for pos in self.visited:
            print(pos)

        for row in reversed(m):
            for col in row:
                print(col, end="")
            print("\n", end="")

    def get_result(self):
        return len(self.visited)


class Cell:
    def __init__(self):
        self.visited = False

    def visit(self):
        self.visited = True

    def __str__(self):
        if self.visited:
            return "#"
        return "."


class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pos = [self.x, self.y]

    def move_to(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = [self.x, self.y]


""" class Grid:
    def __init__(self, matrix):
        self.matrix = matrix
        self.head = Head()
        self.tail = Tail()

    def __str__(self):
        s = ""
        for line in self.matrix:
            s = s + "".join(line) + "\n"
        return s """


def main():
    driver = Driver()
    driver.read()
    driver.execute_moves()
    res = driver.get_result()
    # driver.print_matrix()
    print(res)


if __name__ == "__main__":
    main()
