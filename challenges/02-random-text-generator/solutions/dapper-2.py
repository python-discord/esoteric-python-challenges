# It's too late to apologize for this one

# This is just codegen. Run this and run the resulting file.

import string


BASE = """
def word(*chars):
    return str().join(str(char) for char in chars)

class Letter:
    def __init__(self, descriptor):
        self.d = descriptor

    @property
    def char(self):
        return chr(len(self.d))

    def __str__(self):
        return self.char

"""

SUFFIX = """
print(word(H(), e(), l(), l(), o(), COMMA(), SPACE(), W(), o(), r(), l(), d(), EXCLAMATION_MARK()))

"""

TEMPLATE = """
class {char}(Letter):
    def __init__(self):
        super().__init__({descriptor})

"""

PUNCTUATION = {
 'SPACE': ' ',
 'AMPERSAND': '&',
 'APOSTROPHE': "'",
 'ASTERISK': '*',
 'CIRCUMFLEX_ACCENT': '^',
 'COLON': ':',
 'COMMA': ',',
 'COMMERCIAL_AT': '@',
 'DOLLAR_SIGN': '$',
 'EQUALS_SIGN': '=',
 'EXCLAMATION_MARK': '!',
 'FULL_STOP': '.',
 'GRAVE_ACCENT': '`',
 'GREATER_THAN_SIGN': '>',
 'HYPHEN_MINUS': '-',
 'LEFT_CURLY_BRACKET': '{',
 'LEFT_PARENTHESIS': '(',
 'LEFT_SQUARE_BRACKET': '[',
 'LESS_THAN_SIGN': '<',
 'LOW_LINE': '_',
 'NUMBER_SIGN': '#',
 'PERCENT_SIGN': '%',
 'PLUS_SIGN': '+',
 'QUESTION_MARK': '?',
 'QUOTATION_MARK': '"',
 'REVERSE_SOLIDUS': '\\',
 'RIGHT_CURLY_BRACKET': '}',
 'RIGHT_PARENTHESIS': ')',
 'RIGHT_SQUARE_BRACKET': ']',
 'SEMICOLON': ';',
 'SOLIDUS': '/',
 'TILDE': '~',
 'VERTICAL_LINE': '|'}
def get_desc(char):
    n = ord(char)
    return [[id((lambda: 10001)())]] * n

with open("gen.py", "w", encoding="utf-8") as f:
    f.write(BASE)

    for char in string.ascii_letters:
        f.write(TEMPLATE.format(char=char, descriptor=get_desc(char)))

    for name, char in PUNCTUATION.items():
        f.write(TEMPLATE.format(char=name, descriptor=get_desc(char)))

    f.write(SUFFIX)

