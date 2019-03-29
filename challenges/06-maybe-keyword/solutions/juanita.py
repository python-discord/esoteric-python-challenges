"""
this module is designed to be as seamless to the developer as possible.
once you've imported the module, you will be able to use Maybe. the keyword
is usable in basically any place where True or False are. A SyntaxError is
raised when Maybe is assigned to, deleted, used as an argument name, etc.
"""

import __main__
import dis
import inspect
import random
import sys
import textwrap
from types import CodeType


def _rand_bool():
    return random.choice((True, False))


def _assemble_instructions(instructions):
    """
    Take a list of lists and compile it into a "codestring"
    like the one found at CodeType.co_code. The instructions
    argument should be in the following form:

    [
        [opname, argument],
        ...
    ]

    Extended arguments are handled properly, I believe.
    """

    bytecode = b""
    for instr in instructions:

        opname, arg = instr
        opcode = dis.opmap[opname]

        if arg is None:
            arg = 0

        if arg < 0xff:
            # no fancy business here
            bytecode += bytes([
                opcode, arg
            ])

        else:
            # we want extended args to work though. details are here:
            # https://docs.python.org/3/library/dis.html#opcode-EXTENDED_ARG
            bytecode += bytes([
                dis.opmap["EXTENDED_ARG"],
                arg >> 8,
                opcode,
                arg & 0xff
            ])

    return bytecode


def _mock_syntax_error(message, line_no):
    """
    Output an error which is visually similar to a regular
    SyntaxError. This will refer to a line in the main script.
    """

    # fetch the exact erroneous line of the script.
    with open(__main__.__file__) as script:
        for line in range(line_no - 1):
            script.readline()

        error_line = script.readline().strip()

    sys.stderr.write(textwrap.dedent(f"""\
      File "{__main__.__file__}", line {line_no}
        {error_line}

    SyntaxError: {message}
    """))

    sys.exit(1)


def _implement_maybe(code_object):
    """
    Manipulate the fuck out of a code object to make Maybe a
    perfectly "valid" keyword. This will return a fresh new
    CodeType object with the necessary surgery performed on it.
    Oh, and it implements Maybe recursively. Any code objects
    in the constants of this one will also be mutilated. :)
    """

    # immediately die if Maybe is used as a function parameter name
    argnames = code_object.co_varnames[:code_object.co_argcount]
    if "Maybe" in argnames:
        _mock_syntax_error(
            message="can't use keyword as parameter name",
            line_no=code_object.co_firstlineno
        )

    # add the maybe function to the constants
    new_constants = [*code_object.co_consts, _rand_bool]
    maybe_index = len(new_constants) - 1

    for index in range(maybe_index):
        const = new_constants[index]

        # modify the bytecode recursively if possible.
        if isinstance(const, CodeType):
            new_constants[index] = _implement_maybe(const)

    insert_points = []  # these will be used to realign jump locations
    new_ops = []
    current_line = 0

    for instr in dis.get_instructions(code_object):
        ignore_instr = False

        # keep track of line numbers for making syntax errors
        if instr.starts_line is not None:
            current_line = instr.starts_line

        # it is illegal to use Maybe as a keyword argument
        if instr.opname == "CALL_FUNCTION_KW":
            _, prev_arg = new_ops[-1]

            # check if Maybe is in the list of kwargs
            if "Maybe" in new_constants[prev_arg]:
                _mock_syntax_error(
                    message="keyword can't be an expression",
                    line_no=current_line
                )

        if instr.argval == "Maybe":
            # if this script assigns to Maybe, tell it to bugger off
            if instr.opname.startswith("STORE"):
                _mock_syntax_error(
                    message="can't assign to keyword",
                    line_no=current_line
                )

            # and the same if they're trying to do `del Maybe`.
            if instr.opname.startswith("DELETE"):
                _mock_syntax_error(
                    message="can't delete keyword",
                    line_no=current_line
                )

            # otherwise, replace any access to Maybe with a _rand_bool call
            if instr.opname.startswith("LOAD"):
                # consider everything except "Maybe" strings though, ew.
                if instr.opname != "LOAD_CONST":
                    new_ops.extend([
                        ["LOAD_CONST", maybe_index],
                        ["CALL_FUNCTION", 0]
                    ])  # equivalent to replacing `Maybe` with `_rand_bool()`

                    insert_points.append(instr.offset)
                    ignore_instr = True  # ignore the original instruction

        if not ignore_instr:
            new_ops.append([instr.opname, instr.arg])

    # now go through the instructions and realign any jump locations.
    for index in range(len(new_ops)):
        opname, arg = new_ops[index]
        opcode = dis.opmap[opname]

        if opcode in dis.hasjabs:
            # move the jump location to account for every insertion before it.
            offset = 0
            for point in insert_points:
                if point >= arg:
                    break

                offset += 2

            # then just change the arg of the instruction.
            new_ops[index][1] += offset

        if opcode in dis.hasjrel:
            # same as above, but only consider the insertions between
            # the jump instruction and the jump destination.
            offset = 0
            for point in insert_points:
                # if an insertion occurred between the jump and its
                # destination, make note of the new jump size
                if point >= index * 2:
                    offset += 2

                # anything beyond the jump location won't affect it
                if point > arg:
                    break

            new_ops[index][1] += offset

    # now we can construct the new bytecode... spaghetti incoming :D
    new_code_obj = CodeType(
        # these attributes are unchanged from the original code object
        code_object.co_argcount,
        code_object.co_kwonlyargcount,
        code_object.co_nlocals,
        code_object.co_stacksize,
        code_object.co_flags,

        # these are the only attributes which change
        _assemble_instructions(new_ops),
        tuple(new_constants),

        # then these ones are also unchanged
        code_object.co_names,
        code_object.co_varnames,
        code_object.co_filename,
        code_object.co_name,
        code_object.co_firstlineno,
        code_object.co_lnotab,
        code_object.co_freevars,
        code_object.co_cellvars
    )

    return new_code_obj


def _maybify_main_script():
    """Do all the sorcery. Implements Maybe for __main__."""

    try:
        source = inspect.getsource(__main__)
    except TypeError:
        raise RuntimeError(
            "unable to set up Maybe. are you in a REPL?"
        ) from None

    main_code = compile(source, __main__.__file__, "exec")
    patched_module = _implement_maybe(main_code)

    # now run the new shit as if nothing ever happened :D
    exec(patched_module)
    exit(0)  # stop the *actual* module from running afterwards tho


if __name__ != "__main__":
    _maybify_main_script()
