"""
Just replaces all the `Maybe` strings in your code with `True` or `False` randomly.

example::

```
from zer0 import Maybe

Maybe = 1

>>> Traceback (most recent call last):
>>>   File "zer0.py", line 4
>>>     Maybe = 1
>>>     ^
>>> SyntaxError: can't assign to keyword

print(Maybe)
>>> True
print(Maybe)
>>> False

# Because of the incredibly janky solution, it fails when looping (and probably a lot of other stuff).
for _ in range(3):
    print(Maybe)

>>> True
>>> True
>>> True
```
"""
import inspect
import sys
import traceback

from random import randint


def Maybe():
    return repr(bool(randint(0, 1)))


def __parse_code(lines):
    """Replaces `Maybe` with a random bool in every line"""
    newcode = ''
    for line in lines:
        newline = line.replace('Maybe', Maybe(), 1)
        while 'Maybe' in newline:
            newline = line.replace('Maybe', Maybe(), 1)
        if newline != line and 'import' in newline:
            newline = '\n'
        newcode += newline
    return newcode


def __format_tb():
    """Mock the Exception traceback (not perfect)"""
    tb = traceback.format_exc().splitlines()
    head, _, _, *body = tb
    body = [line.replace('<string>', mod.__file__) for line in body]
    tail = body.pop()

    lineno = int(body[-1].split()[-1]) - 1
    snippet = '    ' + lines[lineno].strip('\n')
    for first, c in enumerate(snippet):
        if c.isalnum():
            break
    pointer = ' ' + ' '*(first-1) + '^'

    return '\n'.join([head]+body+[snippet, pointer, tail])


mod = sys.modules['__main__']
lines, _ = inspect.getsourcelines(mod)
code = __parse_code(lines)


try:
    exec(code, mod.__dict__)
    sys.exit(0)
except Exception:
    print(__format_tb())
    sys.exit(1)
