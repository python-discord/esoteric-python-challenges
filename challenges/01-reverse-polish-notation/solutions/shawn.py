"""
Submission by Shawn

Notes:
Nothing hacky or creative here, just low character count :)
"""

class S:
 def __init__(s):s.s=tuple()
 def m(s,v):s.s=(*s.s,v)
 def p(s):t=s.s[-1];s.s=s.s[:-1];return t
o=lambda z,x,y:{"+":x+y,"−":x-y,"÷":x/(y or 1),"×":x*y}[z]
def f(i):
 n=r=0;s=S()
 for c in i:
  if c.isdigit():n=n*10+int(c);r=1
  elif c==' ':
   if r:s.m(n);n=r=0
  else:s.m(o(c,s.p(),s.p()))
 return s.p()
