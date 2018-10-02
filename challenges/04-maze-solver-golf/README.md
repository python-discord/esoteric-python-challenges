# Challenge 04 - Maze Solver Golf

## Challenge Overview

This week's challenge is fairly straightforward. No esoteric shenanigans or wild restrictions! The task is the following:

Given a maze (in string form) as an input, output the same maze but with the path to the exit. Golf your solution! (make it as short as possible, as in number of characters) Read below for details.

Shout out to Juanita for the idea for this week's challenge!

### Example:

Input:
```
###S###
#     #
## ## #
## ## #
##E####
```

Output:
```
###.###
# ..  #
##.## #
##.## #
##.####
```
## Task:

Create a `function` that takes in *one* argument: A string, representing a 2-dimensional maze. This string will include newline (`\n`) characters.

This function should find the path from the start `S` to the exit `E` and trace it by writing `.`s over the path.

### Details on the characters:

`'S'`:  The start of the maze

`'E'`:  The exit, the end goal

`'#'`:  Walls, you may **not** go through walls (duh)

`' '`:  Empty space. These are the paths you may walk through these

`'.'`:  In the output only, the `.`s indicate the path

### Maze Details:

* The maze may be a rectangle of any dimension
* The maze has exactly one entrace `S` and one exit `E`
* The entrances and exit may be anywhere within the maze, they need not be on the edges
* There is only one solution/path per maze

## Goal:

Golf. (The goal is to create the shortest possible solution, in terms of characters in the source code)

## Restrictions:

No imports, including standard library modules. Only built-ins.

## Submissions Guidelines

* Submit your code as a python file named `<yourname>.py`. If your implementation is too big or you simply prefer splitting the code into several files, submit a directory named `<yourname>` with the code inside. See the `README.md` file in the root of the repository for more information on contributing solutions.

## Tips & Ideas

* There are more than one way to approach this problem. Using the most efficient algorithm might not result in the shortest solution!

## Resources
* ["Maze Solving Algorithm" on Wikipedia](https://en.wikipedia.org/wiki/Maze_solving_algorithm)

Happy Hacking ❤️ Shawn aka Zhawn

## Test Cases

To test your code against test cases (see `README.md` in root of repository for more information on the test runner):

```python
from test_runner import test, case

def my_solution(x, y):
    return x*y

test(my_solution)

case(1, my_solution)
```

# Licensing Information

## By contributing to this repository, you understand and agree that all code in this repository is licensed under the [GNU General Public License, Version 3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.html). 