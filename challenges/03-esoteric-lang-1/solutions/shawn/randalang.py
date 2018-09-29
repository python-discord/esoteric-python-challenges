"""Randalang Interpreter"""
from core import SYMBOLS, T_Type, O_Type
import sys
import random


class Token:
    """Represents source code tokens."""

    def __init__(self, type: T_Type, val) -> None:
        self.type = type
        self.value = val

    def __repr__(self) -> str:
        return f"{self.type} : {self.value}"


class Interpreter:
    """Interprets the list of tokens"""

    def __init__(self, tokens):
        self.tokens = tokens

    def run(self):
        """Interpret the loaded program."""

        def out(m):
            return self.out.append(m)

        def debug(m):
            return self.out.append(m)

        def error(m):
            return self.out.append(m)

        expr_end = (T_Type.ARROW, T_Type.TERM, T_Type.PIPE, T_Type.ND)
        v_stack = []
        i = 0
        skip_to = 0

        while i < len(self.tokens):
            token = self.tokens[i]
            if token.type is T_Type.NUMLITERAL or \
                    token.type is T_Type.STRING:
                v_stack.append(token.value)
            elif token.type is T_Type.ARROW:
                i += 1
                continue
            elif token.type is T_Type.IDENTIFIER:
                expr = []
                while token.type not in expr_end:
                    expr.append(token)
                    i += 1
                    if i >= len(self.tokens):
                        break
                    token = self.tokens[i]
                i -= 1
                f_name = expr[0].value
                # look up identifier in symbols table
                if f_name in SYMBOLS:
                    obj = SYMBOLS[f_name]
                    if obj.type is O_Type.FUNCTION:
                        f_args = expr[1:]
                        for ai, a in enumerate(f_args[:]):
                            if a.value in SYMBOLS:
                                f_args[ai] = SYMBOLS[a.value]
                        ret_val = obj.value(v_stack.pop(),
                                            *f_args)
                        if ret_val is not None:
                            v_stack.append(ret_val)
                    elif obj.type is O_Type.VALUE:
                        v_stack.append(obj.value)
                    else:
                        raise Exception(f"Invalid object type: {obj.type}")
                        break
                else:
                    raise Exception(f"Undefined symbol {token.value}")
                    break
            elif token.type is T_Type.ND:
                j = i+1
                choices = [i]
                if j >= len(self.tokens):
                    break
                token = self.tokens[j]
                while token.type is not T_Type.TERM:
                    if token.type is T_Type.PIPE:
                        choices.append(j)
                    elif token.type is T_Type.ND:
                        skip_to = j
                        break
                    j += 1
                    if j >= len(self.tokens):
                        break
                    token = self.tokens[j]
                target = random.choice(choices)
                i = target
            elif token.type is T_Type.PIPE:
                i = skip_to
            i += 1


class Lexer:
    """Lexes and tokenizes plaintext source."""

    def __init__(self):
        self.tokens = []

    def lex(self, text) -> bool:
        """Lex the source code into a list of tokens."""

        self.tokens = []

        def token(type: T_Type, val):
            """Helper function to reduce typing."""

            self.tokens.append(Token(type, val))

        txt = text.split()  # Ignore *all* whitespace.
        i = 0
        while i < len(txt):
            t = txt[i]
            if t == "->":
                token(T_Type.ARROW, t)
            elif t == "?":
                token(T_Type.ND, t)
            elif t == "|":
                token(T_Type.PIPE, t)
            elif t == ";":
                token(T_Type.TERM, t)
            elif t[0].isdecimal():
                try:
                    val = float(t)
                except Exception as e:
                    print("Invalid num literal", t)
                    return False
                token(T_Type.NUMLITERAL, val)
            elif t[0] == "\"":
                string_buffer = []
                while True:
                    string_buffer.append(t)
                    if t[-1] == "\"":
                        break
                    i += 1
                    t = txt[i]
                token(T_Type.STRING, ' '.join(string_buffer)[1:-1])
            else:
                token(T_Type.IDENTIFIER, t)
            i += 1
        return True

    def get_tokens(self):
        return self.tokens

    def print_tokens(self):
        for i, token in enumerate(self.tokens):
            print(f"{i}: {token.type} : {token.value} ")


def usage():
    """Show usage instructions"""

    print("\nRandalang Interpreter")
    print("Usage:")
    print(
        "\n\tRun from source file: python -f[runs=1] randalang.py <name>.rl")
    print(
        "\n\tRun directly: python -e[runs=1] randalang.py \"<code>\"")
    sys.exit(0)


def run_from_file(file_name, runs=1):
    """Open a file for execution then pass the source to the interpreter."""

    source = ""
    print(f"Opening {file_name} for execution..")
    with open(file_name) as f:
        source = f.read()
    run_source(source, runs)


def run_source(source, runs=1):
    """Interpret the provided source code."""

    lex = Lexer()
    lex.lex(source)
    interp = Interpreter(lex.get_tokens())
    for i in range(runs):
        interp.run()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    mode = None
    runs = 1
    if len(sys.argv[1]) > 2:
        try:
            runs = int(sys.argv[1][2:])
        except ValueError as e:
            usage()
    if sys.argv[1][:2] == "-f":
        run_from_file(sys.argv[2], runs)
    elif sys.argv[1][:2] == "-e":
        run_source(sys.argv[2], runs)
    else:
        usage()
