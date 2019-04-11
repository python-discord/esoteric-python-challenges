# Test Maybe

from maybelib import is_instance as isinstance, Maybe, MaybeSyntaxErrorListener 

msel = MaybeSyntaxErrorListener()
msel.start()

for _ in range(10):
	print(Maybe)

for _ in range(10):
	if Maybe:
		print("And this code might run if it feels like it")

print(isinstance(Maybe, bool))

Maybe = "hello!"
