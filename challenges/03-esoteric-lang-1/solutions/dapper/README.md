# Py-LCI - A Python 3 lambda calculus reducer


## What is lambda calculus?

Lambda calculus is the smallest non-esoteric programming language that is 
Turing-complete. Any problem that can be computed on the fastest supercomputer 
or most powerful machine learning rig can be computed with lambda calculus (
although it will likely be so slow that we would have personal quantum 
computers before it's done).

Learn more at [LearnXinYminutes](https://learnxinyminutes.com/docs/lambda-calculus/), [Wikipedia](https://en.wikipedia.org/wiki/Lambda_calculus), [I Programmer](https://www.i-programmer.info/programming/theory/4514-lambda-calculus-for-programmers.html), or [Palmstrom](http://palmstroem.blogspot.com/2012/05/lambda-calculus-for-absolute-dummies.html).

There is a [short report from FU Berlin](https://www.inf.fu-berlin.de/lehre/WS03/alpi/lambda.pdf) that is also helpful.

## How do I use Py-LCI?

Make sure you are in the root directory and run `python -m dapper` (or run `
__main__.py` from the module directory). This will bring you into an 
REPL session, where you can enter commands or lambda terms.

### Lambda Terms

*λ is interchangeable with a backslash (\\)*

A lambda-term is one of either an application, abstraction, binding, or name.

A **name** is exactly one character, matching the regex `/[^.\\\sλ0-9]/i` (that is, any character excluding numbers `0-9`, whitespace, a period (`.`), a backslash (`\`), and the lambda itself (`λ`)).

An **application** is any terms next to each other. Ex. `l a` applies `a` into `l`.  
*Keep in mind* that lambda calculus is **Left Associative**, so `x y z` is actually `((x y) z)`. Use parentheses to avoid ambiguity.

An **abstraction** is analogous to a function in other languages. It follows the format `λ<name>.<expr>` where `expr` is any lambda-term.

A **binding** is an assignment of an abstraction to a name. Ex. `I = (λx.x)`. Now `I` will refer to `λx.x`.  
Bound names are uppercase by convention.

Py-LCI supports the logical constructs `true`, `false`, `if`, `and`, `or`, and `not`.
When using a logical operator, it should be the first applicator (ex. `(((if true) n) y)` => `n`)

Py-LCI also supports numbers (only integers), but **does not support arithmetic operators** (yet).  
Ex. `(+ 5 (- 8 4))` => `9` 

Function shorthand notation is also supported. That is, `λxyz.x y z` will expand to `λx.(λy.(λz.(x y) z))`

#### Predefined Terms

Py-LCI includes the following terms builtin.

Term                   | Name     | Description
-----------------------|----------|------------
`λy.λx.y(xx) λx.y(xx)` | `Y`      | Y combinator - makes a recursive function out of a nonrecursive function
`λx.x`                 | `I`      | The identity function - returns its parameter unchanged
`x.λy.λz.y(x y z)`     | `succ`   | The successor function - returns the next number after its parameter


### Commands

Help and Quit are self-explanatory.

Set accepts one of three options, and an on/off parameter.

Option      | On               | Off
------------|------------------|----
greeklambda | `(λx.x)`         | `(\x.x)`
showpar     | `(((a b) c) d)`  | `a b c d`
shownormal  | prints a normalization of each term after reduction | does not print normalized terms
showredux   | prints each alpha/beta reduction step | does not print any reduction steps

