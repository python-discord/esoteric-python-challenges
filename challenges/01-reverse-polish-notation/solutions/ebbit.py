""" Reverse Polish calculator for esoteric python challenge 1 by ebbit#0915

The goal is to have a calculator that takes strings in reverse polish notation
and returns the answer without using lists or any imports.
Recognized operators are:
    + for addition,
    − for subtraction,
    ÷ for division
    × for multiplication

Note:
If any input is not entered in correct reverse polish notation:
    If using different operators listed a KeyError is raised.
    If more than (the amount of operators + 1) of digits are entered no
    exceptions will be raised but the returned value could be anything.
    If too many operators are entered IndexError will be raised.
    
EDITOR NOTE:
Breaks 'no list' restriction, but creative solution nonetheless!
"""
def c(i,s=()):
 for t in i.split():
  try:s+=(int(t),)
  except:s=s[:-2]+(eval("s[-2]"+{"+":"+","−":"-","÷":"//","×":"*"}[t]+"s[-1]"),)
 return s[0]
""" uncompacted version:
def calc(inp):

    #define stack as empty tuple
    stack = ()

    #define operators mapped to their their python equivalents
    operator = {"+": "+", "−": "-", "÷": "//", "×": "*"}

    #for each item in the input delimited by spaces
    for token in inp.split():

        #append value to stack as an integer
        try:
            stack += (int(token),)

        #if value is not an integer, find it in the list of operators and
        #evaluate the last two values of the stack with the mapped operator
        #after that replace the two values with the result on the stack
        except ValueError: #a ValueError is raised but an empty except works
            stack = stack[:-2] + (eval("stack[-2]" + operator[token] + "stack[-1]"),)

    #at this point only one value should be on the stack, return it
    return stack[0]
"""
