class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.memory = {}

    def run(self):
        for node in self.ast:

            if node[0] == "LET":
                _, name, value = node
                self.memory[name] = value

            elif node[0] == "PRINT":
                _, value = node

                if value in self.memory:
                    print(self.memory[value])
                else:
                    print(value)
