"""
Submission by Pastebin

Notes:
Requires cpython as this solution generates bytecode
"""

k='*-/+^×−÷';v=b'\x14\0',b'\x18\0',b'\x1b\0',b'\x17\0',b'\x13\0';m=dict(zip(k,v*2));b=b'';e=d='';n=();x=0;s=lambda d,n:d in n and(n,n.index(d))or((*n,d),len(n))
for c in input()+' ':
 if c.isdigit():d+=c
 elif d:x+=1;n,i=s(int(d),n);b+=bytes((100,i));d=e
 if c in m:b+=m[c];x-=1
x-1 and 1/0;f=lambda:0;f.__code__=type(f.__code__)(0,0,0,x,0,b+b'S\0',n,(),(),e,e,0,b);print(f())

"""
Annotated version

m={'+':b'\x17\0','*':b'\x14\0','-':b'\x18\0','/':b'\x1b\0','×':b'\x14\0','−':b'\x18\0','÷':b'\x1b\0'} # map operators to python bytecode that executes that operator
b=b'' # code
d='' # number
n=() # consts
x=0 # number of numbers
o=0 # number of operators
def s(d,n): # search
 try:return(n,n.index(d)) # get the index
 except:return((*n,d),len(n)) # add it
for c in input()+' ': # add space to handle numbers at the end
 if c.isdigit():d+=c
 elif d: # end of a number
    x+=1 # increment number counter
    d=int(d)
    n,i=s(d,n) # search for number in constants
    b+=bytes((100,i)) # 100 = LOAD_CONST
    d='' # reset the number
 if c in m: # operator
    b+=m[c]
    o+=1 # increment operator counter
x-o-1 and 1/0 # if x-o-1 is not 0 then the expression is broken, raise an error
f=lambda:None
f.__code__=type(f.__code__)(0,0,0,x,0,b+b'S\0',n,(),(),'','',0,b'') # create a code object
print(f()) # execute the code object
"""
