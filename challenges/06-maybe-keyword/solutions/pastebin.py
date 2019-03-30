import sys,random
def t(f,e,a):
 # 3.7 ONLY: f.f_trace_opcodes=True
 if e=='call':
  c=f.f_code
  for i,o in enumerate(c.co_code[::2]):
   if o in b'Z[ab'and c.co_names[c.co_code[i*2+1]]=='Maybe':exit()
   elif o in b'}~'and c.co_varnames[c.co_code[i*2+1]]=='Maybe':exit()
 f.f_locals['Maybe']=bool(random.choice([1,0]))
 return t
sys.settrace(t)

'''
Ungolfed version
import sys, random
def trace(frame, event, arg): # settrace stuff
    # 3.7 ONLY: f.f_trace_opcodes=True
    if event == 'call': # function just got called
        code = frame.f_code
        for index, opcode in enumerate(code.co_code[::2]): # only the opcodes, not the args
            # Opcodes in b'Z[ab' perform assignment/deletion on a thing from co_names.
            # If it's messing with Maybe, we don't want that.
            if opcode in b'Z[ab' and code.co_names[code.co_code[index * 2 + 1]] == 'Maybe':
                exit()
            # Same for co_varnames
            elif opcode in b'}~' and code.co_varnames[code.co_code[index * 2 + 1]] == 'Maybe':
                exit()
    frame.f_locals['Maybe'] = bool(random.choice([1, 0])) # Set Maybe in the frame's locals to a random bool
    return trace # settrace stuff
sys.settrace(trace)
'''
