"""
Submission by Shawn aka Zhawn
"""
import itertools
import sys
import dis  # arbitrary modules used to seed the word bank
import random
import string

""" Grab a list of words by combining the __doc__ field of multiple modules

To increase the chance to get real words we filter out strings that are one
or fewer in length and ensure they are alpha only
"""
word_bank = list(filter(lambda w: w.isalpha()
                        and len(w) > 1,
                        (itertools.__doc__.split() + random.__doc__.split()
                         + string.__doc__.split() + sys.__doc__.split()
                         + dis.__doc__.split())))

def get_phrase(length):
    """Return a phrase of the specified length"""
    output = []
    for i in range(length):
        output.append(random.choice(word_bank))
    return (string.whitespace[0].join(output) + string.punctuation[13]).capitalize()

for i in range(10):
    print(get_phrase(5))
