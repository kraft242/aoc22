import re

class driver:
    def __init__(self):
        self.input = []
        self.curr_dir = None
        self.root = None
        self.dirs = []

    def read_input(self):
        with open("input.in", "r") as f:
            self.input = f.read().splitlines()

    def is_command(self, line):
        return line[0] == "$"

    def command_is_ls(self, line):
        return line[1] == "ls"

    def command_is_cd(self, line):
        return line[1] == "cd"

    def command_is_cd_root(self, line):
        return line[2] == "/"

    def command_is_cd_up(self, line):
        return line[2] == ".."

    def is_dir(self, line):
        return line[0] == "dir"

    def add_new_dir(self, line):
        name = line[1]
        new_dir = dir(self.curr_dir, name)
        self.dirs.append(new_dir)
        self.curr_dir.add_subdir(new_dir)

    def add_new_file(self, line):
        size = int(line[0])
        name = line[1]
        new_file = file(self.curr_dir, name, size)
        self.curr_dir.add_file(new_file)

    def execute_command(self, line):
        if self.command_is_ls(line):
            return
        elif self.command_is_cd(line):
            if self.command_is_cd_root(line):
                root_parent = None
                root_name = "/"
                root = dir(root_parent,root_name)
                self.root = root
                self.dirs.append(root)
                self.curr_dir = root
            elif self.command_is_cd_up(line):
                self.curr_dir = self.curr_dir.parent
            else:
                name = line[2]
                new_dir = self.curr_dir.get_subdir(name)
                self.curr_dir = new_dir

    def execute(self):
        for line in self.input:
            line = line.split()
            if self.is_command(line):
                self.execute_command(line)
            elif self.is_dir(line):
                self.add_new_dir(line)
            else:
                self.add_new_file(line)

    def get_result(self):
        res = []
        MAX = 100000
        for dir in self.dirs:
            if dir.size <= MAX:
                res.append(dir.size)
        res_val = sum(res)
        return res_val


    def get_size(self):
        self.root.get_size()


class dir:
    def __init__(self, parent, name):
        self.contents = []
        self.name = name
        self.parent = parent
        self.size = 0

    def add_file(self, file):
        self.contents.append(file)

    def add_subdir(self, dir):
        self.contents.append(dir)

    def get_subdir(self, name):
        for item in self.contents:
            if item.name == name:
                return item

    def get_size(self):
        size = 0
        for item in self.contents:
            size += item.get_size()
        self.size = size
        return size

    def __str__(self):
        sub = ""
        for item in self.contents:
            sub = sub + "\n\t" + str(item)
        return self.name + ": " + str(self.size) + "\n\t" + sub

class file:
    def __init__(self, parent, name, size):
        self.name = name
        self.size = size
        self.parent = parent

    def get_size(self):
        return self.size

    def __str__(self):
        return "    " + self.name + ": " + str(self.size)



def main():
    r = driver()
    r.read_input()
    r.execute()
    r.get_size()
    print(str(r.get_result()))

if __name__ == "__main__":
    main()
