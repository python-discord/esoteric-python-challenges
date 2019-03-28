# Challenge 06 - Maybe?

## Challenge Overview

In search of something new to spice things up, I've decided to make a challenge which isn't about esoteric code. Instead, it's all about esoteric results. We all know that there's two boolean keywords in Python, `True` and `False`, but what if we were a little sneaky and slipped a new one in? For this challenge, I'd like you to use any means you wish to implement a functional `Maybe` keyword. Every time this keyword is accessed, it should present a randomly selected value of `True` or `False` as if there's nothing weird going on.

### Examples

Once you've set up everything needed to get your keyword up and running, the following snippet of code should be valid:

```py
print(Maybe)  # will print True or False randomly.

if Maybe:
    print("And this code might run if it feels like it")

print(isinstance(Maybe, bool))  # will print True, always.

# and just to be consistent with other keywords...
Maybe = "hello!"  # this should raise a SyntaxError immediately, if possible.
```

If it walks like a keyword and quacks like a keyword, then it must be a keyword, right? :D

## Restrictions

None, but do try to avoid any funky business like segfaults and what have you. This implementation of a `Maybe` keyword should be as seamless as you can make it. :)

Ideally, any python file should be able to import all or part of your script in order to gain access to `Maybe` for itself.

## Submissions Guidelines

* Submit your code as a python file named `<yourname>.py` in the `solutions` directory. If your implementation is too big or you simply prefer splitting the code into several files, submit a directory named `<yourname>` with the code inside. See the `README.md` file in the root of the repository for more information on contributing solutions.

Happy Hacking ❤️ Shawn (aka Zhawn) and Juanita

# Licensing Information

## By contributing to this repository, you understand and agree that all code in this repository is licensed under the [GNU General Public License, Version 3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.html).
