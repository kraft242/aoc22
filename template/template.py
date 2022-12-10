class Reader:
    def __init__(self):
        self.input = []

    def read(self):
        file_name = "input.in"
        with open(file_name, "r") as f:
            self.input = f.read().splitlines()

def main():
    pass

if __name__ == "__main__":
    main()