# Authored by Nix
class KInterpreter:
    stack = []
    opcode_pointer = 0

    def dump_stack(self):
        print("Dumping stack:")
        self.stack.reverse()
        [print(element) for element in self.stack]
        self.stack.reverse()

    def eval(self, code, debug=False):
        opcodes = code.split("k?")[:-1]
        while self.opcode_pointer < len(opcodes):
            opcode = opcodes[self.opcode_pointer]
            if debug:
                print("Current opcode is: " + opcode)
                self.dump_stack()
            # add
            if opcode == "+":
                self.stack.append(self.stack.pop() + self.stack.pop())
            # subtract
            elif opcode == "-":
                self.stack.append(self.stack.pop() - self.stack.pop())
            # increment
            elif opcode == "k":
                self.stack.append(self.stack.pop() + 1)
            # decrement
            elif opcode == "n":
                self.stack.append(self.stack.pop() - 1)
            # jump
            elif opcode == "j":
                self.opcode_pointer = self.stack.pop()
            # print
            elif opcode == ">":
                print(chr(self.stack.pop()), end='')
            # input
            elif opcode == "<":
                for char in input().split():
                    self.stack.append(ord(char))
            # delete opcode from opcode list
            elif opcode == "d":
                del opcodes[self.stack.pop()]
            # skip next if value on stack is not 0
            elif opcode == "skni":
                if self.stack.pop():
                    self.opcode_pointer += 1
            # otherwise push ascii integer value of opcode to stack
            else:
                if len(opcode) > 0:
                    self.stack.append(ord(opcode))
                else:
                    print(f"Syntax Error: no instruction: '{opcode}'")
                    self.dump_stack()
                    exit(1)

            self.opcode_pointer += 1
        print("Execution done, dumping stack:")
        while len(self.stack) > 0:
            print(self.stack.pop())
        self.opcode_pointer = 0


                
