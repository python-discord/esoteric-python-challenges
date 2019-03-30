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
