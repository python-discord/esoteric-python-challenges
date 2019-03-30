from maybelib import MaybeBoolean, Maybe, is_instance as isinstance
import threading


class MaybeSyntaxErrorListener(threading.Thread):
	def run(self):
		while True:
			if not isinstance(Maybe, MaybeBoolean):
				raise SyntaxError("can't assign to keyword!")


MSEL = MaybeSyntaxErrorListener()
MSEL.start()


# Test Maybe

for _ in range(10):
	print(Maybe)

for _ in range(10):
	if Maybe:
		print("And this code might run if it feels like it")

print(isinstance(Maybe, bool))

Maybe = "hello!"
