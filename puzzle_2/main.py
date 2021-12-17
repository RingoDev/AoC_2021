def create_area():
    pass


class Sub:
    x = 0
    depth = 0
    aim = 0

    def __repr__(self):
        return f"({self.x},{self.depth}) aim: {self.aim}"

    def up(self, y):
        self.aim = self.aim - y
        pass

    def forward(self, x):
        self.x = self.x + x
        self.depth = self.depth + self.aim * x
        pass


sub = Sub()
print(sub)
with open("input.txt") as file:
    commands = file.read().split("\n")
    for command in commands:
        if command.startswith("up"):
            sub.up(int(command.split(" ")[1]))
        elif command.startswith("down"):
            sub.up(-int(command.split(" ")[1]))
        elif command.startswith("forward"):
            sub.forward(int(command.split(" ")[1]))
        print(command)
        print(sub)
print(f"Result: {sub.x * sub.depth}")
