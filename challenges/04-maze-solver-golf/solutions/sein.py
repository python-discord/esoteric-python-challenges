from test_runner import test, case

# begin challenge code
def f(m,c,l):
	if(not -1<c<len(m)):return 1
	if (m[c] in "S E"):z=m*1;z[c]=".";return "".join(z) if m[c]=="E" else f(z,c+1,l)*f(z,c-1,l)*f(z,c+l,l)*f(z,c-l,l)
	return 1
o=lambda a:f(list(a),a.index("S"),a.index("\n")+1)
#end challenge code

test(o)
