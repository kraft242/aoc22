from math import sqrt as sqrt


class Driver:
    def __init__(self):
        self.visited = []
        self.moves = []
        self.rope = Rope()

    def read(self):
        with open("input.in", "r") as f:
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
        dist = int(self.distance_to_parent(child, parent))
        return dist < 2

    def normalize_visited(self):
        visited = []
        [visited.append(pos) for pos in self.visited if pos not in visited]
        self.visited = visited

    def visit_current_cell(self):
        self.visited.append(self.tail.pos)

    def distance_to_parent(self, child):
        parent = child.parent
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

    def get_parent(self, knot):
        return knot.parent
    
    def move_head(self, move):
        direction = move[0]
        num_steps = move[1]
        for _ in range(num_steps):
            self.visit_current_cell()
            self.move_head_in_direction(direction)
            self.move_child(self.head.child)
        self.visit_current_cell()

    def parent_is_right(self, knot):
        return knot.x + 2 == knot.parent.x and knot.y == knot.parent.y

    def parent_is_left(self, knot):
        return knot.x - 2 == knot.parent.x and knot.y == knot.parent.y

    def parent_is_above(self, knot):
        return knot.x == knot.parent.x and knot.y + 2 == knot.parent.y 

    def parent_is_below(self, knot):
        return knot.x == knot.parent.x and knot.y - 2 == knot.parent.y

    def parent_is_right_above(self, knot):
        return knot.x + 1 == knot.parent.x and knot.y + 2 == knot.parent.y or knot.x + 2 == knot.parent.x and knot.y + 1 == knot.parent.y

    def parent_is_left_above(self, knot):
        return knot.x - 1 == knot.parent.x and knot.y + 2 == knot.parent.y or knot.x - 2 == knot.parent.x and knot.y + 1 == knot.parent.y

    def parent_is_right_below(self, knot):
        return knot.x + 1 == knot.parent.x and knot.y - 2 == knot.parent.y or knot.x + 2 == knot.parent.x and knot.y - 1 == knot.parent.y

    def parent_is_left_below(self, knot):
        return knot.x - 1 == knot.parent.x and knot.y - 2 == knot.parent.y or knot.x - 2 == knot.parent.x and knot.y - 1 == knot.parent.y

    def apply_child_move(self, knot):
        right = self.parent_is_right(knot)
        left = self.parent_is_left(knot)
        above = self.parent_is_above(knot)
        below = self.parent_is_below(knot)
        right_above = self.parent_is_right_above(knot)
        left_above = self.parent_is_left_above(knot)
        right_below = self.parent_is_right_below(knot)
        left_below = self.parent_is_left_below(knot)
        x = knot.x
        y = knot.y
        if right_above:
            knot.move_to([x + 1, y + 1])
            return
        elif left_above:
            knot.move_to([x - 1, y + 1])
            return
        elif right_below:
            knot.move_to([x + 1, y - 1])
            return
        elif left_below:
            knot.move_to([x - 1, y - 1])
            return
        elif right:
            knot.move_to([x + 1, y])
            return
        elif left:
            knot.move_to([x - 1, y])
            return
        elif above:
            knot.move_to([x, y + 1])
            return
        elif below:
            knot.move_to([x, y - 1])
            return

    def get_distance_to_parent(self, knot):
        parent = knot.parent
        parent_x = parent.x
        parent_y = parent.y
        knot_x = knot.x
        knot_y = knot.y
        dx = parent_x - knot_x
        dy = parent_y - knot_y
        return dx,dy


    def move_child(self, knot):
        dx, dy = self.get_distance_to_parent(knot)
        abs_dx = abs(dx)
        abs_dy = abs(dy)
        new_x = knot.x
        new_y = knot.y
        if abs_dx == 2:
            if dx == 2:
                new_x = knot.x + 1
            elif dx == -2:
                new_x = knot.x - 1
        if abs_dy == 2:
            if dy == 2:
                new_y = knot.y + 1
            elif dy == -2:
                new_y = knot.y - 1
        if abs_dx == 1:
            if dx == 1:
                if dy == 2:
                    new_x = knot.x + 1
                    new_y = knot.y + 1
                elif dy == -2:
                    new_x = knot.x + 1
                    new_y = knot.y - 1
            elif dx == -1:
                if dy == 2:
                    new_x = knot.x - 1
                    new_y = knot.y + 1
                elif dy == -2:
                    new_x = knot.x - 1
                    new_y = knot.y - 1
        if abs_dy == 1:
            if dy == 1:
                if dx == 2:
                    new_x = knot.x + 1
                    new_y = knot.y + 1
                elif dx == -2:
                    new_x = knot.x - 1
                    new_y = knot.y + 1
            elif dy == -1:
                if dx == 2:
                    new_x = knot.x + 1
                    new_y = knot.y - 1
                elif dx == -2:
                    new_x = knot.x - 1
                    new_y = knot.y - 1

        knot.move_to([new_x, new_y])
        if knot.child is None:
            self.visit_current_cell()
            return
        return self.move_child(knot.child)
        """ dist = self.distance_to_parent(knot)
        if dist == 2:
            parent_x = knot.parent.x
            parent_y = knot.parent.y
            knot_x = knot.x
            knot_y = knot.y
            diff_x = parent_x - knot_x
            diff_y = parent_y - knot_y
            if diff_x == 2:
                knot_x = knot_x + 1
            if diff_y == 2:
                knot_y = knot_y + 1
            knot.move_to([knot_x, knot_y])
        if knot.child is None:
            self.visit_current_cell()
            return
        return self.move_child(knot.child) """
        """ parent = knot.parent
        diff = [abs(parent.x) - abs(knot.x), abs(parent.y) - abs(knot.y)]
        diff_x = diff[0]
        diff_y = diff[1]
        new_pos = [knot.x, knot.y]
        # Parent is above
        if diff_y == 2:
            # Parent is right above
            if diff_x == 2:
                new_pos = [knot.x + 1, knot.y + 1]
            # Parent is left above
            elif diff_x == -2:
                new_pos = [knot.x - 1, knot.y + 1]
            # Parent is straight above
            else:
                new_pos = [knot.x, knot.y + 1]
        # Parent is below
        elif diff_y == -2:
            # Parent is right below
            if diff_x == 2:
                new_pos = [knot.x + 1, knot.y - 1]
            # Parent is left below
            elif diff_x == -2:
                new_pos = [knot.x - 1, knot.y - 1]
            # Parent is straight below
            else:
                new_pos = [knot.x, knot.y - 1]
        # Parent ist straigh left
        elif diff_x == -2:
            new_pos = [knot.x - 1, knot.y]
        # Parent is straight right
        else:
            new_pos = [knot.x + 1, knot.y]
        knot.move_to(new_pos)
        if knot.child == None:
            self.visit_current_cell()
            return
        return self.move_child(knot.child) """

        """ if not self.child_is_adjacent_to_parent(knot):
            parent_prev_pos = knot.parent.prev_pos
            knot.move_to(parent_prev_pos)
        if knot.child == None:
            self.visit_current_cell()
            return
        return self.move_child(knot.child)"""

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
        self.prev_pos = [self.x,self.x]

    def move_to(self, pos):
        self.prev_pos = self.pos
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
