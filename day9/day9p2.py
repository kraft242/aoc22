from math import sqrt as sqrt


class Driver:
    def __init__(self):
        self.visited = []
        self.moves = []
        self.rope = Rope()

    def read(self):
        with open("example.in", "r") as f:
            for line in f.read().splitlines():
                line = line.split(" ")
                line[1] = int(line[1])
                self.moves.append(line)

    def execute_moves(self):
        for move in self.moves:
            self.rope.move_head(move)
        visited = self.rope.visited
        self.visited = self.normalize_visited(visited)

    def normalize_visited(self, visited):
        res = []
        [res.append(pos) for pos in visited if pos not in res]
        return res

    def print_moves(self):
        for pos in self.visited:
            print(pos)

    def get_result(self):
        return len(self.visited)


class Rope:
    def __init__(self):
        self.visited = []
        num_knots = 10
        self.knots = [Knot(i) for i in range(num_knots)]
        parent = None
        for knot in self.knots:
            knot.parent = parent
            parent = knot
        child = None
        for knot in reversed(self.knots):
            knot.child = child
            child = knot

        for knot in self.knots:
            print("Knot number: " + str(knot) + ", parent: " + str(knot.parent) + ", child: " + str(knot.child))
        self.head = self.knots[0]
        tail_index = num_knots - 1
        self.tail = self.knots[tail_index]

    def child_is_adjacent_to_parent(self, child):
        parent = child.parent
        dist = int(self.distance(parent, child))
        return dist < 2

    def normalize_visited(self):
        visited = []
        [visited.append(pos) for pos in self.visited if pos not in visited]
        self.visited = visited

    def visit_current_cell(self):
        self.visited.append(self.tail.pos)

    def distance(self, parent, child):
        parent_x = parent.x
        parent_y = parent.y
        child_x = child.x
        child_y = child.y
        dx = abs(parent_x - child_x)
        dy = abs(parent_y - child_y)
        return int(max(dx, dy))

    def move_head_in_direction(self, direction):
        pos = self.head.pos
        x = pos[0]
        y = pos[1]
        # Right
        if direction == "R":
            new_pos = [x + 1, y]
        # Up
        elif direction == "U":
            new_pos = [x, y + 1]
        # Left
        elif direction == "L":
            new_pos = [x - 1, y]
        # Down
        else:
            new_pos = [x, y - 1]
        self.head.move_to(new_pos)
        return pos

    def move_head(self, move):
        direction = move[0]
        num_steps = move[1]
        for _ in range(num_steps):
            pos = self.move_head_in_direction(direction)
            self.move_child(self.head, pos)
            #self.print_matrix()

    def move_child(self, knot, parent_pos):
        if knot.child == None:
            self.visit_current_cell()
            return
        pos = knot.pos
        child = knot.child
        if not self.child_is_adjacent_to_parent(child):
            child.move_to(parent_pos)
        return self.move_child(child, pos)

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
        print("")


class Knot:
    def __init__(self, num):
        self.num = num
        self.x = 0
        self.y = 0
        self.child = None
        self.pos = [self.x, self.y]

    def move_to(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = [self.x, self.y]

    def __str__(self):
        return str(self.num)


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
