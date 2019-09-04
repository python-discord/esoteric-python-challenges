'''
This implements the classic BF language using lists and slicing on the list class
[][
 [[]]::[[]] # starts bf program
][
 []:[]:[] # equivalent to ","
][
 [] # equivalent to "."
][
 [[]] # runs the program
]

the above program takes in one character and outputs it. 
other implemented commands are:
:[]:[] # which is ">"
[]:[]: # which is "<"
[]::[] # which is "+"
:[]: # which is "-"
[]:: # which is "["
::[] # which is "]"
'''

from ctypes import *
import sys
import traceback

binaryfunc = CFUNCTYPE(py_object, py_object, py_object)

mapping = c_void_p.from_address(id(list) + 112)

original_ptr = c_void_p.from_address(mapping.value + 8)
original_method = cast(original_ptr, binaryfunc)

bfStarted = False
bfStr = []

@binaryfunc
def new_method(self, item):
    global bfStarted, bfStr
    if item == slice([[]],None,[[]]):
       bfStarted = True
       bfStr = []
       
       
    if bfStarted:
       if item == slice(None,[],[]):bfStr.append('>')
       elif item == slice([],[],None):bfStr.append('<')
       elif item == slice([],None,[]):bfStr.append('+')
       elif item == slice(None,[],None):bfStr.append('-')
       elif item == []:bfStr.append('.')
       elif item == slice([],[],[]):bfStr.append(',')
       elif item == slice([],None,None):bfStr.append('[')
       elif item == slice(None,None,[]):bfStr.append(']')
       elif item == [[]]:
          if bfStr:
             bfStarted = False
             (lambda f:(lambda f,a=[],p=[],c=[]:(lambda b,q={},i=[]:[q.update({'>':lambda:[p.append(p.pop()+1),a.append(0) if p[0]==len(a) else None],'<':lambda:p.__setitem__(0,p[0]-1 if p[0]>0 else 0),'+':lambda:a.__setitem__(p[0],a[p[0]]+1 if a[p[0]] < 255 else 0),'-':lambda:a.__setitem__(p[0],a[p[0]]-1 if a[p[0]] > 0 else 256),'.':lambda:print(chr(a[p[0]]),end=''),',':lambda:a.__setitem__(p[0],[0 if i else i.extend(input()),ord(i.pop(0)) if i else 0][1]),'[':lambda:None if a[p[0]] else c.append(b[c.pop()]),']':lambda:c.append(b[c.pop()]) if a[p[0]] else None}),[*map(lambda x:[x.clear(),x.append(0)],(a,p,c))],[*iter(lambda:[q[f[c[0]]](),c.append(c.pop()+1),c[0]<len(f)][2],0)]][0])((lambda s=[],b={}:[s.clear(),b.clear(),[[s.append(p)if c == '[' else 0,b.update({s[-1]:p,p:s.pop()})if c == ']' else 0]for p,c in enumerate(f)],b][3])()))(''.join(filter(lambda x:x in '><+-.,[]',f))))(''.join(bfStr))
             bfStr = []
          return
       return self
    
    tb = []   
    with type('',(),{'__enter__':lambda self:None,'__exit__':lambda self,*args:not tb.extend(args)})():
       return list.__getitem__(self,item)
    
    traceback.print_exception(*tb)

new_method_ptr = cast(new_method, c_void_p)
original_ptr.value = new_method_ptr.value
