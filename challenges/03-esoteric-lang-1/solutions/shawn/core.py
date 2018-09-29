from enum import Enum


def _fadd(x, y, *args):
    return x+y.value


def _fsub(x, y, *args):
    return x-y.value


def _fdiv(x, y, *args):
    return x/y.value


def _fmul(x, y, *args):
    # coerce y into an int if x is a string
    if type(x) is str:
        y.value = int(y.value)
    return x*y.value


def _fpow(x, y, *args):
    return x**y.value


def _frem(x, y, *args):
    return x % y.value


def _fprint(x, *args):
    print(x)


def _fcrash(*args):
    return 1/0


def _fcompare(x, y, *args):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


class O_Type(Enum):
    """Object Types."""
    FUNCTION = 0
    VALUE = 1


class T_Type(Enum):
    """Token Types."""
    ARROW = 0
    ND = 1
    PIPE = 2
    NUMLITERAL = 3
    IDENTIFIER = 4
    TERM = 5
    STRING = 6
    COND = 7


class Object:
    """Code objects"""

    def __init__(self, otype: O_Type, name: str, desc: str, value) -> None:
        self.type = otype
        self.name = name
        self.desc = desc
        self.value = value


def _fassign(x, y, *args):
    if y.type is T_Type.NUMLITERAL:
        y.value = float(y.value)
    SYMBOLS[x] = Object(O_Type.VALUE, x, "", y.value)
    return None


_add = Object(O_Type.FUNCTION, "add", "add the two arguments", _fadd)
_sub = Object(O_Type.FUNCTION, "sub", "subtract arg 2 from arg 1", _fsub)
_div = Object(O_Type.FUNCTION, "div", "divide arg 1 by arg 2", _fdiv)
_mul = Object(O_Type.FUNCTION, "mul", "multiply arg 1 by arg 2", _fmul)
_pow = Object(O_Type.FUNCTION, "pow", "raise arg 1 to power arg 2", _fpow)
_rem = Object(O_Type.FUNCTION, "rem", "remainder of arg 1 div by arg 2", _frem)
_print = Object(O_Type.FUNCTION, "print", "print the value to screen", _fprint)
_assign = Object(O_Type.FUNCTION, "assign", "assign a value to iden", _fassign)
_crash = Object(O_Type.FUNCTION, "crash", "kill the program", _fcrash)

SYMBOLS = {
    'set': _assign,
    '=': _assign,
    'add': _add,
    '+': _add,
    'sub': _sub,
    '-': _sub,
    'mul': _mul,
    '*': _mul,
    'div': _div,
    '/': _div,
    'pow': _pow,
    '**': _pow,
    'rem': _rem,
    '%': _rem,
    'print': _print,
    'crash': _crash
}
