# Randalang


*Randalang* is a turing-incomplete, random, non-deterministic computing engine platform.. Okay fine it's just a dumb language with branches that are chosen randomly.

## Instructions

Run from console:
`python randalang.py -e[runs=1] "3 -> ? + 1 | - 2 ? -> print ;"`

Run from source file:
`python randalang.py -f[runs=1] sourcefile.rl`

## Syntax and what not:

This language has no formal grammar and consists of a crappily hacked-together interpreter that probably has countless bugs unaccounted for, but here's some basic guidelines :)

* Programs are described as a flow of data, with `->` essentially meaning take the value on the left and apply it as an argument to the function to the right
* Tokens/Symbols are separated by spaces. Extra space is discarded which means that string literals can have at most one space between characters, call it a feature
* The only values that can be defined are numeric literals (floats) and string literals (delimited by double quotes `"string"`)
* Values can be stored to a symbol (aka assigned to a variable) by using the function `set` or `=`
* Non-Deterministic program segments (which are really just different possible sequences of function calls that are chosen at random) are delimited by `?`s and the options themselves by `|`. See examples

## Quick Examples

Assign a value to a symbol, then print it
```
"x" -> set "Banana" ;
x -> print ;
```

Take a number, and nondeterministically subtract 5, add 5, or times 5
```
6 ->
? - 5
| + 5
| * 5
? -> print ;
```
Note that the ignored extra whitespace allows to format the program as desired

Another example showing pretty much all of the features, and demonstrating that a "choice path" can have more than one operation:

```
"y" -> = 5 ;
"x" -> = 2.5 ;
x ->
? + 2 -> - y
| * 2 -> ** y
| + y
? -> print ;
```