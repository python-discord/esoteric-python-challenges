# Lambda calculus reducer

# Copyright (c) 2018 AnonymousDapper

# Do whatever you want with this source, but include the copyright line.

__version__ = "0.0.1f"

import readline, os

from pprint import pprint

from lark.exceptions import UnexpectedInput

from .parser import LCIParser


def print_help():
    print((
        "Py-LCI version %s (Type Help for help, Quit to quit)\n"
        "\n"
        "Type a lambda term to compute its normal form, or enter one"
        "of the following commands:"
        "\n"
        "Help                   Print this help message\n"
        "Quit                   Exit Py-LCI\n"
        "Set option (on|off)    Set interpreter options. Valid options are:\n"
        "                       showpar, showredux, greeklambda, shownormal\n"
    ) % __version__)

def get_dict(item):
    cache = {}

    for k,v in item.__dict__.items():
        if isinstance(v, (str, int, float, bool)) or v is None:
            cache[k] = v

        else:
            cache[k] = get_dict(v)

    return cache

def repl():
    parser = LCIParser()

    print("Py-LCI version %s (Type Help for help, Quit to quit)" % __version__)
    while True:
        try:
            source = input("py-lci> ")

            if source.startswith("Quit"):
                print("Closed.")
                break

            elif source.startswith("Help"):
                print_help()
                continue

            elif source.startswith("Set"):
                args = source.split()

                if len(args) != 3:
                    print("Command error: Set takes 2 parameters")
                    continue

                parser.set_opt(*args[1:])
                continue

            elif source == "":
                continue

            try:
                tree = parser.parse(source)

            except UnexpectedInput as e:
                print("Err: Unexpected input near '%s':" % source[e.pos_in_stream])
                print(e.get_context(source, 12))
                continue

            except Exception as e:
                print("Err: %s" % str(e))
                continue

            original = str(tree)
        
            reduced = parser.alpha_reduce(tree)
            reduced = parser.beta_reduce(reduced)

            print("\n%s\n\t-> %s" % (original, str(reduced)))

            if parser.get_opt("showredux"):
                print("(%d substitutions, %d reductions)" % (parser.substitutions, parser.reductions) )

            if parser.get_opt("shownormal"):
                print("  Normalized: %s" % parser.get_repr(reduced))

        except KeyboardInterrupt:
            print("Closed.")
            return


repl()
