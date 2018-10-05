# Lambda calculus reducer runtime

# Sources:

# https://www.inf.fu-berlin.de/lehre/WS03/alpi/lambda.pdf

# http://www.cs.yale.edu/homes/hudak/CS201S08/lambda.pdf

# https://github.com/bdevorem/lamby

from lark import Lark, Transformer, v_args

import copy

GRAMMAR_FILE = "lc.lark"

class LVariable:
    def __init__(self, name, bound=False):
        self.name = name.value if hasattr(name, "value") else str(name)
        self.bound = bound

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, LVariable):
            return self.name == other.name

        return False

    def __contains__(self, other):
        return self == other

    @property
    def normalform(self):
        return True

class LApplication:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def __str__(self):
        showpar = LCIParser.get_opt("showpar")

        return "%s%s %s%s" %("(" * showpar, self.left, self.right, ")" * showpar)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, LApplication):
            return (self.left == other.left) and (self.right == other.right)

        return False

    def __contains__(self, other):
        if isinstance(other, LVariable):
            if (isinstance(self.left, LVariable) and other == self.left) or (isinstance(self.right, LVariable) and other == self.right):
                return True

            if isinstance(self.left, LAbstraction):
                return other in self.right

            elif isinstance(self.right, LAbstraction):
                return other in self.left

        return False

    @property
    def normalform(self):
        if isinstance(self.left, LAbstraction):
            return False

        elif isinstance(self.left, LApplication):
            return self.left.normalform

        else:
            return True

class LAbstraction:
    def __init__(self, var, body, const=None):
        self.var = var
        self.body = body
        self._const = const

        self.identity = var == body

    def __str__(self):
        if self._const is None:
            showpar = LCIParser.get_opt("showpar")
            greeklambda = LCIParser.get_opt("greeklambda")

            return "%s%s%s.%s%s" % ("(" * showpar, "λ" if greeklambda else "\\", self.var, self.body, ")" * showpar)

        return self._const

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, LAbstraction):
            return (self.var == other.var) and (self.body == other.body)

        return False

    @property
    def normalform(self):
        return True

# αβδεφγηιθκλμνοπχρστυωξψζ

#  λy.λx.y(xx) λx.y(xx)
Y_COMB = LAbstraction(LVariable("Y"), LAbstraction(LVariable("X"), LApplication(LApplication(LVariable("Y"), LApplication(LVariable("X"), LVariable("X"))), LAbstraction(LVariable("X"), LApplication(LVariable("Y"), LApplication(LVariable("X"), LVariable("X")))))), const="Y")

# λx.x
IDENTITY = LAbstraction(LVariable("X"), LVariable("X"))

# λx.λy.x
TRUE = LAbstraction(LVariable("X"), LAbstraction(LVariable("Y"), LVariable("X")), const="true")

# λx.λy.y
FALSE = LAbstraction(LVariable("X"), LAbstraction(LVariable("Y"), LVariable("Y")), const="false")

# λx.λy.λz.x y z
IF = LAbstraction(LVariable("X"), LAbstraction(LVariable("Y"), LAbstraction(LVariable("Z"), LApplication(LApplication(LVariable("X"), LVariable("Y")), LVariable("Z")))), const="if")

# λx.λy.if x true y
AND = LAbstraction(LVariable("X"), LAbstraction(LVariable("Y"), LApplication(LApplication(LApplication(IF, LVariable("X")), TRUE), LVariable("Y"))), const="and")

# λx.λy.if x y false
OR = LAbstraction(LVariable("X"), LAbstraction(LVariable("Y"), LApplication(LApplication(LApplication(IF, LVariable("X")), LVariable("Y")), FALSE)), const="or")

# λx.if x false true 
NOT = LAbstraction(LVariable("X"), LApplication(LApplication(LApplication(IF, LVariable("X")), FALSE), TRUE), const="not")


# Arithmetic

# λx.λy.λz.y(x y z)
SUCC = LAbstraction(LVariable("X"), LAbstraction(LVariable("Y"), LAbstraction(LVariable("Z"), LApplication(LVariable("Y"), LApplication(LApplication(LVariable("X"), LVariable("Y")), LVariable("Z"))))), const="succ")

# λs.λz.z
ZERO = LAbstraction(LVariable("S"), LAbstraction(LVariable("Z"), LVariable("Z")), const="0")

class ConstHandler:
    bindings = {
        "0": ZERO,
        "Y": Y_COMB,
        "I": IDENTITY
    }

    constants = {
        "true": TRUE,
        "false": FALSE,
        "if": IF,
        "and": AND,
        "or": OR,
        "not": NOT,
        "succ": SUCC
    }

    _equivalence_cache = {}

    CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    CHAR_IDX = 0

    @staticmethod
    def expand_abstraction(*args):
        body = args[-1:][0]
        rvars = list(args[:-1])

        assert len(rvars) > 0

        abstraction = LAbstraction(rvars.pop(), body)

        while len(rvars) > 0:
            abstraction = LAbstraction(rvars.pop(), abstraction)

        return abstraction

    @classmethod
    def get_const(cls, name):
        return cls.constants[name]

    @classmethod
    def set_bind(cls, name, expr):
        expr._const = name.value
        cls.bindings[name] = expr

        return expr

    @classmethod
    def get_bind(cls, name):
        return cls.bindings.get(name.value, LVariable(name))

    def register_hvar(self, name):
        char = name.value

        if char in self.CHARS:
            self.CHARS.remove(char)

        return LVariable(name)

    def get_number(self, number):
        number = number.value

        if number not in self.bindings:
            tmp = LAbstraction(LVariable("S"), LAbstraction(LVariable("Z"), LVariable("Z")))
            new_num = int(number)

            if new_num > 989:
                raise RuntimeError("Integers must be less than 989")

            for x in range(new_num):
                tmp.body.body = LApplication(LVariable("S"), tmp.body.body)

            tmp._const = number

            print("New num", tmp)

            self.set_bind(number, tmp)

        else:
            tmp = self.bindings[number]

        return tmp

    def get_replacement(self):
        if self.CHAR_IDX < len(self.CHARS):
            char = self.CHARS[self.CHAR_IDX]
            self.CHAR_IDX += 1

            return LVariable(char)

        raise RuntimeError("Too many colliding names. Try simplifying your expression")

    def _get_term_repr(self, term):
        if isinstance(term, LVariable):
            name = term.name

            if name not in self._equivalence_cache:
                self._equivalence_cache[name] = str(len(self._equivalence_cache))

            return [self._equivalence_cache[name]]

        elif isinstance(term, LApplication):
            left = self._get_term_repr(term.left)
            right = self._get_term_repr(term.right)

            return ["A", *left, *right]

        elif isinstance(term, LAbstraction):
            return ["Y", *self._get_term_repr(term.var), ".", *self._get_term_repr(term.body)]

    def get_term_repr(self, term):
        self._equivalence_cache = {}

        return "".join(self._get_term_repr(term))


@v_args(inline=True)
class LambdaTransformer(Transformer):
    apply = lambda self, left, right: LApplication(left, right)
    abstract = lambda self, *args: self._const_handler.expand_abstraction(*args)
    constant = lambda self, name: self._const_handler.get_const(name)
    bind = lambda self, name, expr: self._const_handler.set_bind(name, expr)
    name = lambda self, name: self._const_handler.get_bind(name)
    hvar = lambda self, name: self._const_handler.register_hvar(name)

    num = lambda self, number: self._const_handler.get_number(number)

    def __init__(self, const_handler):
        self._const_handler = const_handler


class LCIParser:
    OPTS = {
        "greeklambda": True,
        "showpar": True,
        "showredux": True,
        "shownormal": True
    }

    @classmethod
    def set_opt(cls, name, val): 
        lval = val.lower()

        if lval == "off":
            nval = False

        elif lval == "on":
            nval = True

        else:
            print("Unrecognized status %s, (Set option on|off)" % val)
            return

        nname = name.lower()

        if nname in cls.OPTS:
            cls.OPTS[nname] = nval

            print("%s is now %s" % (nname, lval))

    @classmethod
    def get_opt(cls, name):
        if name.lower() in cls.OPTS:
            return cls.OPTS[name.lower()]

    def __init__(self):
        self.parser = None
        self.lark_kwargs = dict(
            rel_to=__file__,
            debug=True,
            start="start",
            lexer="contextual",
            parser="lalr"
        )

        self.substitutions = 0
        self.reductions = 0

        self.const_handler = None

    def _setup_parser(self):
        self.substitutions = 0
        self.reductions = 0

        self.const_handler = ConstHandler()

        self.parser = Lark.open(GRAMMAR_FILE, transformer=LambdaTransformer(self.const_handler), **self.lark_kwargs)

    def parse(self, source):
        self._setup_parser()

        return self.parser.parse(source)

    def get_repr(self, term):
        return self.const_handler.get_term_repr(term)

    # Alpha reduction functions
    def recurse_alpha_replace(self, term, old, repl):
        if isinstance(term, LVariable):
            if term == old:

                return repl

        elif isinstance(term, LApplication):
            term.left = self.recurse_alpha_replace(term.left, old, repl)
            term.right = self.recurse_alpha_replace(term.right, old, repl)

        elif isinstance(term, LAbstraction):
            if term.var == old:
                term.var = self.recurse_alpha_replace(term.var, old, repl)

            term.body = self.recurse_alpha_replace(term.body, old, repl)

        return term

    def check_collision(self, term, var):
        if isinstance(term, LApplication):
            self.check_collision(term.left, var)
            self.check_collision(term.right, var)

        elif isinstance(term, LAbstraction):
            if term.var == var:
                self.recurse_alpha_replace(term, var, self.const_handler.get_replacement())
                return

            self.check_collision(term.body, var)

    def recurse_alpha_reduce(self, term):
        if isinstance(term, LVariable):
            return term

        elif isinstance(term, LAbstraction):
            term.body = self.recurse_alpha_reduce(term.body)

            return term

        elif isinstance(term, LApplication):
            if isinstance(term.left, LAbstraction) and isinstance(term.right, LVariable):
                self.check_collision(term.left, term.right)

            term.left = self.recurse_alpha_reduce(term.left)
            term.right = self.recurse_alpha_reduce(term.right)

        return term

    def alpha_reduce(self, term):
        if isinstance(term, (LVariable, LAbstraction)):
            return term

        else:
            tmp = term


            while True:
                tmp_str = str(tmp)
                reduced = self.recurse_alpha_reduce(tmp)
                
                if str(reduced) == tmp_str:
                    return tmp

                tmp = reduced
                self.substitutions += 1

                if self.get_opt("showredux"):
                    print("  α > %s" % term)


    # Beta reduction functions
    def recurse_beta_replace(self, term, old, repl):
        if isinstance(term, LVariable):
            if term == old:

                return repl

        elif isinstance(term, LApplication):
            term.left = self.recurse_beta_replace(term.left, old, repl)
            term.right = self.recurse_beta_replace(term.right, old, repl)

        elif isinstance(term, LAbstraction):
            if term.var == old:
                return term

                term.var = self.recurse_beta_replace(term.var, old, repl)

            term.body = self.recurse_beta_replace(term.body, old, repl)

        return term

    def recurse_beta_reduce(self, term):
        if isinstance(term, (LVariable, LAbstraction)):
            return term

        elif isinstance(term, LApplication):
            if isinstance(term.left, LAbstraction):
                return self.recurse_beta_replace(term.left.body, term.left.var, term.right)

            new_left = self.recurse_beta_reduce(term.left)

            if new_left != term.left:
                term.left = new_left

            else:
                term.right = self.recurse_beta_reduce(term.right)

            return term

    def beta_reduce(self, term):
        if isinstance(term, (LVariable, LAbstraction)):
            return term

        else:
            tmp = term

            while True:
                tmp_str = str(tmp)
                reduced = self.recurse_beta_reduce(tmp)

                if str(reduced) == tmp_str:
                    return tmp

                tmp = reduced
                self.reductions += 1

                if self.get_opt("showredux"):
                    print("  β > %s" % term)
