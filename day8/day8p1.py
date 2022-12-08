class Tree:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.visible = False
        self.visited = False

    def make_visible(self):
        self.visible = True

    def visit(self):
        self.visited = True


class Forest:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.total_number_trees = self.height * self.width
        self.num_visible_trees = 0

    def is_edge(self, x, y):
        return x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1

    def mark_visible_trees(self):
        for y, row in enumerate(self.matrix):
            for x, tree in enumerate(row):
                if self.is_edge(x, y):
                    tree.make_visible()
                    self.num_visible_trees += 1
                elif self.clear_horizontal_line(tree) or self.clear_vertical_line(tree):
                    tree.make_visible()
                    self.num_visible_trees += 1
        return self.num_visible_trees

    def clear_vertical_line(self, tree):
        x = tree.x
        y = tree.y
        col = [row[x] for row in self.matrix]
        above = col[:y]
        below = col[y+1:]
        return self.clear_sub_line(tree, above) or self.clear_sub_line(tree, below)

    def clear_horizontal_line(self, tree):
        x = tree.x
        y = tree.y
        row = self.matrix[y]
        left = row[:x]
        right = row[x+1:]
        return self.clear_sub_line(tree, left) or self.clear_sub_line(tree, right)

    def clear_sub_line(self, tree, sub):
        for neighbor in sub:
            if tree.height <= neighbor.height:
                return False
        return True


class Driver:
    def __init__(self):
        self.input = []
        self.forest = None
        self.matrix = None

    def read_input(self):
        input_file = "input.in"
        read_mode = "r"
        with open(input_file, read_mode) as f:
            lines = f.read().splitlines()
            matrix = []
            for y, line in enumerate(lines):
                row = [Tree(x, y, int(n)) for x, n in enumerate(line)]
                matrix.append(row)
        self.forest = Forest(matrix)

    def get_result(self):
        print(self.forest.mark_visible_trees())

    def print_visible(self):
        for row in self.forest.matrix:
            for col in row:
                if col.visible:
                    print(col.height, end="")
                else:
                    print(" ", end="")
            print("\n", end="")


def main():
    driver = Driver()
    driver.read_input()
    driver.get_result()
    driver.print_visible()


if __name__ == "__main__":
    main()
