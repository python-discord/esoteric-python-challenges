#!/bin/python3

# required only on windows
import colorama as colour

colour.init()

## base code ##

# import sys


# colour_order = [
#     ["255", "0", "0"],
#     ["255", "128", "0"],
#     ["255", "255", "0"],
#     ["128", "255", "0"],
#     ["0", "255", "0"],
#     ["0", "255", "128"],
#     ["0", "255", "255"],
#     ["0", "128", "255"],
#     ["0", "0", "255"],
#     ["128", "0", "255"],
#     ["255", "0", "255"],
#     ["255", "0", "128"],
# ]

# file_name = sys.argv[1]
# with open(file_name) as file:
#     data = file.read().split("\n")

# max_char = max(len(line) for line in data) + len(data)

# for y, line in enumerate(data):
#     for x, char in enumerate(line):
#         position = (x + y) * 11 // max_char
#         print(f'\033[38;2;{";".join(colour_order[position])}m{char}', end="")
#     print()

## minified code ##
# fmt: off
c=[[255,0,0],[255,128,0],[255,255,0],[128,255,0],[0,255,0],[0,255,128],[0,255,255],[0,128,255],[0,0,255],[128,0,255],[255,0,255],[255,0,128]]
y=0
import sys
p=print
d=open(sys.argv[1]).read().split('\n');n=len(d);w=max(len(l)for l in d);m=w+n;d=[(i+' '*w)[:w]for i in d]
while y<n:
 x=0
 while x<w:r,g,b=c[(x+y)%12];p(f'\033[38;2;{r};{g};{b}m{d[y][x]}',end='');x+=1
 y+=1;p()
