"""Weird encoder/obfuscator that came up to my mind.
The method is, for every character in a string,
convert it to two random characters like that,
so sum of ord() calls is equal to ord() of the plain character.
"""

import random

def wrap(string: str, width: int = 2):
    for n in range(0, len(string), width):
        yield string[n:n+width]

def encode(string: str):
    final = ''
    for char in string:
        o = ord(char)
        x = random.randrange(0, o)
        y = o - x
        final += chr(x) + chr(y)
    return final

def decode(string: str):
    final = ''
    for chars in wrap(string):
        final += chr(sum(map(ord, chars)))
    return final

# compressed decoder, one-lined for readability purposes
decoder = "(lambda s:''.join(chr(sum(map(ord, c)))for c in (s[n:n+2]for n in range(0,len(s),2))))({!r})"

if __name__ == '__main__':
    print('Evaluate the following code to get the source:', decoder.format(encode(input('Enter the code to obfuscate: '))))
