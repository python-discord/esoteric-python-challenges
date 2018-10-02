"""🤔 lang is an esolang designed to fuel the hatred of emojis, by ebbit

🤔 lang should be pronounced "u+1F914 lang" or "colon thinking colon lang" on
Discord, "please no thank you" also suffices.
🤔 can be easily used in python with the unicode escape as '\\U0001f914'.
🤔 lang code consists entirely of unicode emojis :
Unicode defines emojis in character range 1F600 - 1F64F.
There's also a lot of extra symbols used as emojis in the 1F300 - 1F5FF range.
Also some extra emojis in the supplemental section 1F900 - 1F9FF but this range
also has a lot of empty characters that are not defined.
263A is the original smiley face as defined in miscellaneous symbols, it does
nothing.
The interpreter function will not accept any character outside of these ranges.
Every operation, variable or literal is a single emoji, there are no
indentations, separators or line breaks, there are only emojis.
The first range is used to represent the integers 0-80, other numbers can only
be defined by using the results of other functions.
The second range is used as variable names, only 767 variables can be defined as
there are only that many emojis in that range.
Operations are defined in the third range, call help for a full list of
operations.
If a variable is not defined the next result will initialize it and immediately
return the variable's value.
If a variable is defined it's current value is returned.
Operations will always return a single value.
Execution is recursive, RecursionError is the only error that could happen
during normal execution.
Even though no errors are thrown if something odd happens it will almost never
do what you want.
Enjoy! \u263A

Commandline use:
Ether pass a script as text as an argument or pipe it like
"python __file__ <scriptfile"

Examples:
💥🤓🤚🌀🤝😅😅🤧🤚🌀🤒💥🤨🤐🌀🤢🌀
will print 25 explosions then 24 etc. until it reaches 0.

🤒🤔🤨🤖
will quickly learn you that trying to read input is useless here.
"""
import sys
from random import randint
_debug = 0

ops = []

def set_op(fun):
    """decorator to set a function as an operator function"""
    if _debug:
        def wrap(*args):
            print(fun.__name__)
            return fun(*args)
        wrap.__doc__ = fun.__doc__
        ops.append(wrap)
    else:
        ops.append(fun)
    return fun

class Code():
    """represents a \U0001f914lang program"""

    def __init__(self, text):
        self.index = -1
        self.start = self.index
        self.defs = {}
        self.text = text

    def ready(self):
        """check if there still is code to execute"""
        return self.index < len(self.text)

    def next(self):
        """move index and return next operation"""
        self.index += 1
        return self.text[self.index]

    def get(self):
        """get next operation safely"""
        try:
            return self.next()
        except IndexError:
            return 0

    def make(self, name):
        """create temporary variable with name"""
        self.defs[name] = ret = self.exec()
        return ret

    def has(self, op):
        """has variable op defined"""
        return op in self.defs

    def access(self, op):
        """fetch a stored value"""
        try:
            value = self.defs[op]
        except IndexError:
            return 0
        try:
            ret = value.run(self)
            value.restore()
            return ret
        except AttributeError:
            return value

    @set_op
    def set(self):
        """set a variable to the next result

        The variable used to assign the function to is the next emoji, if the
        next emoji is not a variable this operation will not bind to anything
        but it will be evaluated the same way.
        If the same variable is set again while busy setting itself it will be
        overwritten.
        """
        name = self.get()
        if name not in names:
            self.index -= 1
            return self.exec()
        self.defs[name] = ret = self.exec()
        return ret

    @set_op
    def print(self):
        """print the next result as emoji"""
        ret = self.exec()
        sys.stdout.write(chr(first_int + ret % total_ints))
        return ret

    @set_op
    def ext_print(self):
        """print the next result as miscellaneous symbol or pictograph"""
        ret = self.exec()
        sys.stdout.write(chr(first_name + ret % total_names))
        return ret

    @set_op
    def prev_symbol(self):
        """interpret the previous symbol as int"""
        try:
            return ord(self.text[self.index - 1]) - first_name
        except IndexError:
            return 0

    @set_op
    def read(self):
        """read a character code from input"""
        try:
            return ord(sys.stdin.read(1))
        except Exception:
            return 0

    @set_op
    def save(self):
        """save the current code location"""
        self.start = self.index
        return self.exec()

    @set_op
    def load(self):
        """load the previously saved code location"""
        self.index = self.start
        return self.exec()

    @set_op
    def repeat_load(self):
        """repeat loading next result times"""
        for i in range(self.exec()):
            self.load()
        return self.exec()

    @set_op
    def sub_load(self):
        """load the saved code location then continue from current location"""
        prev = self.index
        ret = self.load()
        self.index = prev
        return ret

    class _function:
        def __init__(self, index, *args):
            self.args = args
            self.index = index

        def run(self, code):
            self.res = code.index
            prev = code.defs
            defs = {name: code.exec() for name in self.args}
            code.defs = {**code.defs, **defs}
            code.index = self.index
            ret = code.exec()
            code.defs = prev
            return ret

        def restore(*self):
            code.index = self.res

    @set_op
    def function(self):
        """save the next result as a function to be used again later

        The variable used to assign the function to is the next emoji, if the
        next emoji is not a variable this operation will not bind to anything
        but it will be evaluated the same way.
        If more variables are specified they will be used as arguments.
        Arguments can not be default initialized, when a function is called it
        will simply take amount of arguments of results.
        Variables initialized inside of the function will remain within the
        function and not be saved outside it, allowing you to use temporary
        values!
        If the same variable is set again while busy setting itself it will be
        overwritten.
        Functions are allowed to call themselves, this usually causes an
        unbreakable loop, it's a feature.
        Remember that the function is immediately called on init.
        """
        name = self.get()
        args = []
        if name in names:
            while True:
                e = self.get()
                if e not in names:
                    break
                args.append(e)
        else:
            name = None
        self.index -= 1
        fun = Code._function(self.index, *args)
        if name:
            self.defs[name] = fun
        return fun.run(self)

    @set_op
    def repeat(self):
        """get the next result then repeat the operation after that and return
        the average of all the results, as int
        
        if the next result is less than one, this statement is ignored
        """
        amount = max(self.exec(), 1)
        get = 0
        prev = self.index
        for i in range(amount):
            self.index = prev
            get += self.exec()
        return get // amount

    @set_op
    def add(self):
        """add the next two results"""
        return self.exec() + self.exec()

    @set_op
    def sub(self):
        """subtract the next two results"""
        return self.exec() - self.exec()

    @set_op
    def mul(self):
        """multiply the next two results"""
        return self.exec() * self.exec()

    @set_op
    def pow(self):
        """get the result of raising the first result to the second result
        power, rounded"""
        return int(self.exec() ** self.exec())

    @set_op
    def choose(self):
        """get the results of the next two operations and then return the first
        if the next result is 0 else return the second"""
        a = self.exec()
        return self.exec() if self.exec() else a

    @set_op
    def rand(self):
        """returns a random emoji number"""
        return randint(0, total_ints - 1)

    @set_op
    def inc(self):
        """increments next value by one"""
        return self.exec() + 1

    @set_op
    def dec(self):
        """decrements next value by one"""
        return self.exec() - 1

    @set_op
    def wrap(self):
        """wraps the next value to fit in the emoji range"""
        return self.exec() % total_ints

    @set_op
    def ez_div(self):
        """return the next value divided by the value after that, except when
        either is 0, 0 will be returned immediately"""
        a = self.exec()
        if a:
            b = self.exec()
            if b:
                return a // b
        return 0

    @set_op
    def ez_mod(self):
        """return the next value modulo divided by the value after that, except
        when either is 0, 0 will be returned immediately"""
        a = self.exec()
        if a:
            b = self.exec()
            if b:
                return a % b
        return 0

    @set_op
    def bor(self):
        """return the next value bitwise orred with the one after that"""
        return self.exec() | self.exec()

    @set_op
    def band(self):
        """return the next value bitwise anded with the one after that"""
        return self.exec() & self.exec()

    @set_op
    def flush(self):
        """flush stdout"""
        sys.stdout.write("\n")
        return self.exec()


if len(ops) > 47:
    raise SyntaxError("too many operations defined in interpreter: " + len(ops))

first_int = ord("\U0001f600")
total_ints = 80
ints = [chr(first_int + i) for i in range(total_ints)]
first_name = ord("\U0001f300")
total_names = first_int - first_name
names = [chr(i) for i in range(first_name, first_int)]
first_fun = ord("\U0001f910")
fun = {chr(first_fun + i): item for i, item in enumerate(ops)}
op_names = [*fun]
op_names.sort()
nop = "\u263a"

def exec(code):
    """executes a \U0001f914lang code object"""
    try:
        op = code.next()
    except IndexError:
        return 0
    if op in fun:
        return fun[op](code)
    if op in ints:
        return ints.index(op)
    if code.has(op):
        return code.access(op)
    if op in names:
        return code.make(op)
    if op == nop:
        return exec(code)
    raise ValueError("unrecognized operation {}".format(op))

Code.exec = exec


def eval(text):
    """interpret a \U0001f914lang script as text"""
    code = Code(text)
    ret = 0
    while code.ready():
        ret = code.exec()
    return ret

def help():
    """return a list of all operators and their docs"""
    doc = "These are all the operations recognized by the interpreter:\n"
    for name in op_names:
        op = fun[name]
        doc += "\nemoji {} or u+{}:\n".format(name, hex(ord(name)))
        for line in op.__doc__.split("\n"):
            if line:
                doc += "    " + line.strip() + "\n"
    return doc
__doc__ += "\n" + help()

def random_input(amount = 1000):
    """return amount characters of random valid \U0001f914lang code"""
    all_ops = [nop, *names[:10], *ints[:30], *fun]
    return tuple(all_ops[randint(0, len(all_ops) - 1)] for i in range(amount))

def ez_translate(normie_text):
    """convenience function that transfers normie text to emoji, also removes
    whitespace"""
    s = ("`1234567890qwertyuiopasdfghjkl;zxcvbnm,./"
           "~!@#$%^&*()QWERTYUIOPASDFGHJKL:ZXCVBNM<>?")
    emo = {s[i]: e for i, e in enumerate([*ints[:11], *names[:30], *op_names])}
    ret = ""
    for char in normie_text:
        try:
            ret += emo[char]
        except KeyError:
            ret += char.strip()
    return ret

if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        for arg in args:
            print(eval(arg))
    else:
        print(eval(input()))

