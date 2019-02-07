# Lovely Printer

The idea here is simple: You have a program that prints things. Now you can have a program that prints things in the shape of a heart!

## Usage

The main usage is via context manager that temporarily overrides the builtin `print`. 
That is, you should be able to use this with any existing program that uses `print`! How lovely!

Suppose you have your normal boring program

```python
# my_program.py
def main():
    print('This is just an example')
```
Make it lovely like so

```python
from lovely_printer import lovely_print
from my_program import main

with lovely_print():
    main()
# then print returns to normal
print("Isn't that lovely?")
```

Then you should see the output something like

```
 This    is 
j    u s    t
      a     n
           e
  x       a
   m     p
    l   e
     T h
      i

Isn't that lovely?
```
