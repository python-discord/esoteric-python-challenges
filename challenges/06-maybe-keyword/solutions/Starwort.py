__all__ = ["Maybe"]

import random


class _Maybe:
    def __repr__(self):
        return repr(random.choice([True, False]))

    def __getattribute__(self, *args, **kwargs):
        return random.choice([True, False]).__getattribute__(*args, **kwargs)

    def __del__(self):
        import sys
        if sys.meta_path is not None:  # squash interpreter errors
            import os
            os._exit(1)

    def __bool__(self):
        return random.choice([True, False])

    def __eq__(self, other):
        return random.choice([True, False]) == other

class MaybeWrapper:
    Maybe = _Maybe()

    def __setattr__(self, name, value):
        if name == 'Maybe':
            raise SyntaxError("can't assign to keyword")
        else:
            super().__setattr__(name,value)

    def __delattr__(self, name):
        if name == 'Maybe':
            raise SyntaxError("can't delete keyword")
        else:
            super().__delattr__(name)

Maybe = _Maybe()

if __name__ == "__main__":

    print(Maybe)  # will print True or False randomly.

    if Maybe:
        print("And this code might run if it feels like it")

    print(isinstance(Maybe, bool))  # will print True, always.

    # and just to be consistent with other keywords...
    Maybe = "hello!"  # this should raise a SyntaxError immediately, if possible.
else:
    import sys
    sys.modules[__name__] = MaybeWrapper()
