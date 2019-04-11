import __main__
from random import choice
from threading import Thread

class MaybeBoolean():
	def __repr__(self):
		return choice(["True", "False"])

	def __bool__(self):
		return choice([True, False])

def is_instance(obj1, obj2):
	if isinstance(obj1, MaybeBoolean):
		return True
	return isinstance(obj1, obj2)

class MaybeSyntaxErrorListener(Thread):
	def run(self):
		while True:
			if not isinstance(__main__.Maybe, MaybeBoolean):
				raise SyntaxError("can't assign to keyword!")

Maybe = MaybeBoolean()
