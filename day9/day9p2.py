from math import sqrt as sqrt


class Driver:
    def __init__(self):
        self.moves = []
        self.visited = []
        self.head = Knot(None)
        num_children = 9
        parent = self.head
        self.children = []
        for _ in range(num_children):
            knot = Knot(parent)
            self.children.append(knot)
            parent = knot
        self.tail = self.children[8]

    def read(self):
        with open("example.in", "r") as f:
            for line in f.read().splitlines():
                line = line.split(" ")
                line[1] = int(line[1])
                self.moves.append(line)

    def execute_moves(self):
        for move in self.moves:
            self.move_parent(move)
            direction = move[0]
            num_steps = move[1]
            for _ in range(num_steps):
                self.visit_current_cell()
                parent_pos = self.move_head_in_direction(direction)
                for child in self.children:
                    parent_pos = child.parent.pos
                    if not self.child_is_adjacent(child):
                        parent_pos = self.move_child(child, parent_pos)
                    parent_pos = parent_pos
            self.visit_current_cell()
        self.normalize_visited()

    def move_parent(self, move):
        direction = move[0]
        num_steps = move[1]
        for _ in range(num_steps):
            pass

    def move_child(self, child, pos):
        old_pos = child.pos
        child.move_to(pos)
        return old_pos

    def child_is_adjacent(self, child):
        parent = child.parent
        dist = int(self.distance(parent, child))
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

    def distance(self, parent, child):
        child_x = child.x
        child_y = child.y
        parent_y = parent.x
        parent_y = parent.y
        dx = abs(parent_y - child_x)
        dy = abs(parent_y - child_y)
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

    def print_moves(self):
        for pos in self.visited:
            print(pos)

    def print_matrix(self):
        height = 5
        width = 6
        m = [["." for _ in range(width)] for _ in range(height)]
        for pos in self.visited:
            x = pos[0]
            y = pos[1]
            m[y][x] = "#"

        for row in reversed(m):
            for col in row:
                print(col, end="")
            print("\n", end="")

    def get_result(self):
        return len(self.visited)


""" class Rope:
    def __init__(self):
        self.head = Knot(None)
        num_children = 9
        self.children = []
        for n in range(num_children):
            knot = Knot(n)
            self.children.append(knot) """


class Knot:
    def __init__(self, parent):
        self.x = 0
        self.y = 0
        self.parent = parent
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
    driver.print_moves()
    # driver.print_matrix()
    print(res)


if __name__ == "__main__":
    main()
