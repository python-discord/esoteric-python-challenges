import builtins
from textwrap import dedent
from unittest import mock
from contextlib import contextmanager
from itertools import cycle
_print = builtins.print

TEMPLATE_HEART = dedent('''
 ####   ####
#    # #    #
#     #     #
 #         #
  #       #
   #     #
    #   #
     # #
      #
''')


def to_hearts(text):
    chars = cycle(list(text))
    num_hearts = (len(text) // TEMPLATE_HEART.count('#')) + 1
    for heart in range(num_hearts):
        lines = []
        for line in TEMPLATE_HEART.split('\n'):
            while '#' in line:
                line = line.replace('#', next(chars), 1)
            lines.append(line)
        yield '\n'.join(lines)


def _lovely_print(*things_to_print, **kwargs):
    things_to_print = list(things_to_print)
    for thing in things_to_print:
        for heart in to_hearts(thing):
            _print(heart, **kwargs)


@contextmanager
def lovely_print(*args, **kwargs):
    with mock.patch('builtins.print', new=_lovely_print) as m:
        yield m


if __name__ == '__main__':
    with lovely_print():
        print('Hello World!')
        print('I do not like', 'green eggs and ham')
        print('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
