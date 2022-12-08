class Tree:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.visible = False
        self.visited = False
        self.scenic_score = 0

    def make_visible(self):
        self.visible = True

    def visit(self):
        self.visited = True


class Forest:
    def __init__(self, matrix):
        self.matrix = matrix
        self.trees = []
        for row in self.matrix:
            for tree in row:
                self.trees.append(tree)
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.total_number_trees = self.height * self.width
        self.num_visible_trees = 0

    def is_edge(self, x, y):
        return x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1

    def calculate_scenic_score(self):
        for y, row in enumerate(self.matrix):
            for x, tree in enumerate(row):
                if self.is_edge(x, y):
                    tree.scenic_score = 0
                else:
                    tree.scenic_score = self.get_scenic_score(tree)

    def get_max_scenic_score(self):
        max = 0
        for tree in self.trees:
            if tree.scenic_score > max:
                max = tree.scenic_score
        return max

    def mark_visible_trees(self):
        for y, row in enumerate(self.matrix):
            for x, tree in enumerate(row):
                if self.is_edge(x, y):
                    tree.make_visible()
                    self.num_visible_trees += 1
                elif self.get_horizontal_score(tree) or self.get_vertical_score(tree):
                    tree.make_visible()
                    self.num_visible_trees += 1
        return self.num_visible_trees

    def get_scenic_score(self, tree):
        vertical_score = self.get_vertical_score(tree)
        horizontal_score = self.get_horizontal_score(tree)
        total_score = vertical_score[0] * vertical_score[1] * \
            horizontal_score[0] * horizontal_score[1]
        return total_score

    def get_vertical_score(self, tree):
        x = tree.x
        y = tree.y
        col = [row[x] for row in self.matrix]
        above = reversed(col[:y])
        below = col[y+1:]
        return [self.clear_sub_line(tree, above), self.clear_sub_line(tree, below)]

    def get_horizontal_score(self, tree):
        x = tree.x
        y = tree.y
        row = self.matrix[y]
        left = reversed(row[:x])
        right = row[x+1:]
        return [self.clear_sub_line(tree, left), self.clear_sub_line(tree, right)]

    def clear_sub_line(self, tree, sub):
        score = 0
        for neighbor in sub:
            score += 1
            if tree.height <= neighbor.height:
                return score
        return score


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
        self.forest.calculate_scenic_score()
        max_score = self.forest.get_max_scenic_score()
        return max_score

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
    res = driver.get_result()
    print(res)


if __name__ == "__main__":
    main()
