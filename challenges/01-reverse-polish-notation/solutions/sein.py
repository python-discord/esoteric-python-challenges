#begin challenge code
def f(s):
	s=" "+s;p=s.rfind(" ");c=s[:p];w=s[p:]
	try:return c,int(w)
	except:o=f(c);g=f(o[0]);return g[0],eval(f"{g[1]}{w}{o[1]}")
o=lambda s:f(s)[1]
#end challenge code

# begin tests
assert(o("1")==1)
assert(o("2 2 +")==4)
assert(o("2 3 + 1 -")==4)
assert(o("15 7 1 1 + - / 3 * 2 1 1 + + -")==5)
assert(o("420 1337 + 1 -")==1756)
# end tests
