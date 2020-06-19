import random

class MaybeMeta(type):
    def __bool__(self):
        return random.choice((True, False))
class Maybe(metaclass=MaybeMeta):
    ...
    
