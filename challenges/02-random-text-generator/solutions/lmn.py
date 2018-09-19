import contextlib as ___________
import io as ____________
import random as _________

__________ = _________.sample.__doc__.splitlines()[-3].strip().split()[0].lower()

_ = ____________.StringIO()
with ___________.redirect_stdout(_):
    __import__(__________)

_ = _.getvalue()
__ = _[3]
___ = _[17]
____ = _.splitlines()[2][-1]
_____ = _.splitlines()[2:]
______ = _.splitlines()[14].split()[3][-1]
_______ = __.join(_________.choice(_____).split()[:2])
________ = __.join(_________.choice(_____).split()[2:4]).strip(____ + ______)
_________ = __.join(_________.choice(_____).split()[1:5]).strip(____ + ______)

print(_______ + __ + ________ + ___ + __ + _________ + ____)