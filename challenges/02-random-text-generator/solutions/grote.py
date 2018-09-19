import random
"""
Submission by Grote
"""

import random
import string
import threading
import multiprocessing
import re

zero = int()
two = len(re.__name__)
one = int(str(len(multiprocessing.__name__))[zero])
space = string.whitespace[zero]
words = [a.strip(string.punctuation) for a in dir(random) + dir(string) + dir(threading) + dir(multiprocessing) + dir(re)]

def random_phrase(length):
    while(length > zero):
        length -= one
        print(random.choice(words), end=space)

random_phrase(17)