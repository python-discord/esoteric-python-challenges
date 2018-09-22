# Challenge 03 - Esoteric Language (1)

## Challenge Overview

> An esoteric programming language (ess-oh-terr-ick), or esolang, is a computer programming language designed to experiment with weird ideas, to be hard to program in, or as a joke, rather than for practical use. (from [esolangs.org](https://esolangs.org/wiki/Esoteric_programming_language) )

The archetypal/most famous esolang is known as [*brainfuck*](https://esolangs.org/wiki/Brainfuck), and here is (a version) of the `hello world` program written in BF:

`++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.`

Beautiful, isn't it? To find out how it works, visit the link above. Of course, esolangs can be weird (as is the case with BF) but they can also just be experimental, funny, absurd, etc. 

## Task:

Create and(or) implement an esoteric language of your own!

## Goal:

Have fun and get creative!

## Restrictions:

None!

## More info.

This week's challenge is the first in what I hope could be a series of esolang-related challenges. This week's challenge is not necessarily *hard*, but has a higher entrance barrier. Either on your own or with someone else, devise and implement an esoteric programming language. This is a Python challenge, so all tools related to your esolang must be written in Python, whether you write a simple compiler, interpreter, etc.

Inventing a language, even esoteric, can be a daunting task. Therefor, you also have the option of implementing [an already existing language](https://esolangs.org/wiki/Language_list). 

Since this challenge is more involved than the ones I usually post, feel free to take as much time as you need, even if new challenges are posted, challenges don't expire.

## Submissions Guidelines

* Submit your code as a python file named `<yourname>.py`. If your implementation is too big or you simply prefer segregating the code into several files, submit a directory named `<yourname>` with the code inside.
* Add comments that document what language you have implemented (if not your own), how the language works, and how to use the implementation.

## Tips & Ideas

* Browse already existing esolangs for inspiration!
* The language you create can be very simple!
* Implementing an existing esolang can be simpler than it seems. *BF* can be implemented with a couple of lists, a few variables and a bunch of `if` statements.
* You can write an interpreter for your language but you could also write a transpiler that outputs Python code or, even more complex, cpython *bytecode*.
* Share your ideas with others!

## Resources
* [esolangs.org - The most comprehensive esolang resource](https://esolangs.org/wiki/Main_Page)
* [The Super Tiny Compiler on Github](https://github.com/jamiebuilds/the-super-tiny-compiler) Albeit being written in JavaScript, this short write-up describes in a simple way the general phases that a compiler goes through to go from source to end product. Can be useful if you want to write a lexer/Abstract Syntax Trees and need a little inspiration

Happy Hacking ❤️ Shawn aka Zhawn