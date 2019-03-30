from random import choice

class MaybeBoolean():
	def __repr__(self):
		return choice(["True", "False"])

	def __bool__(self):
		return choice([True, False])

def is_instance(obj1, obj2):
	if isinstance(obj1, MaybeBoolean):
		return True
	return isinstance(obj1, obj2)

Maybe = MaybeBoolean()
