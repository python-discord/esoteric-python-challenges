'''This is a module, preferably with the filename "Maybe.txt", so that you can just type "import Maybe" and it'll all be done. There will be an instance of the Might_Be class stored under the name "Maybe". Alternatively, you can run the module on it's own and do your coding afterwards. That should work too.
This doesn't meet the final condition of forbidding assignment to Maybe.
Made by IFcoltransG'''

import random, sys

def _val():
    #gets the random boolean
    #used each time a method of Maybe is called, to return a different value
    return bool(random.randrange(2))

class Might_Be(int):
    def __call__(self):
        #a bit different from a normal boolean — allows you to use "var_name = Maybe()"
        #even though you can just use "var_name = Maybe"
        return self
    #a bunch of stuff copied from the int class using:
    '''for method in dir(bool()):
        print(f"def {method}(self, *args, **kwargs):\n    return _val().{method}(*args, **kwargs)\n")'''
    #although you don't really need the trailing \n, and also need to indent the result
    #also, I deleted __new__ because it caused problems
    def __abs__(self, *args, **kwargs):
        return _val().__abs__(*args, **kwargs)
    
    def __add__(self, *args, **kwargs):
        return _val().__add__(*args, **kwargs)
    
    def __and__(self, *args, **kwargs):
        return _val().__and__(*args, **kwargs)
    
    def __bool__(self, *args, **kwargs):
        return _val().__bool__(*args, **kwargs)
    
    def __ceil__(self, *args, **kwargs):
        return _val().__ceil__(*args, **kwargs)
    
    def __class__(self, *args, **kwargs):
        return _val().__class__(*args, **kwargs)
    
    def __delattr__(self, *args, **kwargs):
        return _val().__delattr__(*args, **kwargs)
    
    def __dir__(self, *args, **kwargs):
        return _val().__dir__(*args, **kwargs)
    
    def __divmod__(self, *args, **kwargs):
        return _val().__divmod__(*args, **kwargs)
    
    def __doc__(self, *args, **kwargs):
        return _val().__doc__(*args, **kwargs)
    
    def __eq__(self, *args, **kwargs):
        return _val().__eq__(*args, **kwargs)
    
    def __float__(self, *args, **kwargs):
        return _val().__float__(*args, **kwargs)
    
    def __floor__(self, *args, **kwargs):
        return _val().__floor__(*args, **kwargs)
    
    def __floordiv__(self, *args, **kwargs):
        return _val().__floordiv__(*args, **kwargs)
    
    def __format__(self, *args, **kwargs):
        return _val().__format__(*args, **kwargs)
    
    def __ge__(self, *args, **kwargs):
        return _val().__ge__(*args, **kwargs)
    
    def __getattribute__(self, *args, **kwargs):
        return _val().__getattribute__(*args, **kwargs)
    
    def __getnewargs__(self, *args, **kwargs):
        return _val().__getnewargs__(*args, **kwargs)
    
    def __gt__(self, *args, **kwargs):
        return _val().__gt__(*args, **kwargs)
    
    def __hash__(self, *args, **kwargs):
        return _val().__hash__(*args, **kwargs)
    
    def __index__(self, *args, **kwargs):
        return _val().__index__(*args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        return _val().__init__(*args, **kwargs)
    
    def __init_subclass__(self, *args, **kwargs):
        return _val().__init_subclass__(*args, **kwargs)
    
    def __int__(self, *args, **kwargs):
        return _val().__int__(*args, **kwargs)
    
    def __invert__(self, *args, **kwargs):
        return _val().__invert__(*args, **kwargs)
    
    def __le__(self, *args, **kwargs):
        return _val().__le__(*args, **kwargs)
    
    def __lshift__(self, *args, **kwargs):
        return _val().__lshift__(*args, **kwargs)
    
    def __lt__(self, *args, **kwargs):
        return _val().__lt__(*args, **kwargs)
    
    def __mod__(self, *args, **kwargs):
        return _val().__mod__(*args, **kwargs)
    
    def __mul__(self, *args, **kwargs):
        return _val().__mul__(*args, **kwargs)
    
    def __ne__(self, *args, **kwargs):
        return _val().__ne__(*args, **kwargs)
    
    def __neg__(self, *args, **kwargs):
        return _val().__neg__(*args, **kwargs)
    
    def __or__(self, *args, **kwargs):
        return _val().__or__(*args, **kwargs)
    
    def __pos__(self, *args, **kwargs):
        return _val().__pos__(*args, **kwargs)
    
    def __pow__(self, *args, **kwargs):
        return _val().__pow__(*args, **kwargs)
    
    def __radd__(self, *args, **kwargs):
        return _val().__radd__(*args, **kwargs)
    
    def __rand__(self, *args, **kwargs):
        return _val().__rand__(*args, **kwargs)
    
    def __rdivmod__(self, *args, **kwargs):
        return _val().__rdivmod__(*args, **kwargs)
    
    def __reduce__(self, *args, **kwargs):
        return _val().__reduce__(*args, **kwargs)
    
    def __reduce_ex__(self, *args, **kwargs):
        return _val().__reduce_ex__(*args, **kwargs)
    
    def __repr__(self, *args, **kwargs):
        return _val().__repr__(*args, **kwargs)
    
    def __rfloordiv__(self, *args, **kwargs):
        return _val().__rfloordiv__(*args, **kwargs)
    
    def __rlshift__(self, *args, **kwargs):
        return _val().__rlshift__(*args, **kwargs)
    
    def __rmod__(self, *args, **kwargs):
        return _val().__rmod__(*args, **kwargs)
    
    def __rmul__(self, *args, **kwargs):
        return _val().__rmul__(*args, **kwargs)
    
    def __ror__(self, *args, **kwargs):
        return _val().__ror__(*args, **kwargs)
    
    def __round__(self, *args, **kwargs):
        return _val().__round__(*args, **kwargs)
    
    def __rpow__(self, *args, **kwargs):
        return _val().__rpow__(*args, **kwargs)
    
    def __rrshift__(self, *args, **kwargs):
        return _val().__rrshift__(*args, **kwargs)
    
    def __rshift__(self, *args, **kwargs):
        return _val().__rshift__(*args, **kwargs)
    
    def __rsub__(self, *args, **kwargs):
        return _val().__rsub__(*args, **kwargs)
    
    def __rtruediv__(self, *args, **kwargs):
        return _val().__rtruediv__(*args, **kwargs)
    
    def __rxor__(self, *args, **kwargs):
        return _val().__rxor__(*args, **kwargs)
    
    def __setattr__(self, *args, **kwargs):
        return _val().__setattr__(*args, **kwargs)
    
    def __sizeof__(self, *args, **kwargs):
        return _val().__sizeof__(*args, **kwargs)
    
    def __str__(self, *args, **kwargs):
        return _val().__str__(*args, **kwargs)
    
    def __sub__(self, *args, **kwargs):
        return _val().__sub__(*args, **kwargs)
    
    def __subclasshook__(self, *args, **kwargs):
        return _val().__subclasshook__(*args, **kwargs)
    
    def __truediv__(self, *args, **kwargs):
        return _val().__truediv__(*args, **kwargs)
    
    def __trunc__(self, *args, **kwargs):
        return _val().__trunc__(*args, **kwargs)
    
    def __xor__(self, *args, **kwargs):
        return _val().__xor__(*args, **kwargs)
    
    def bit_length(self, *args, **kwargs):
        return _val().bit_length(*args, **kwargs)
    
    def conjugate(self, *args, **kwargs):
        return _val().conjugate(*args, **kwargs)
    
    def denominator(self, *args, **kwargs):
        return _val().denominator(*args, **kwargs)
    
    def from_bytes(self, *args, **kwargs):
        return _val().from_bytes(*args, **kwargs)
    
    def imag(self, *args, **kwargs):
        return _val().imag(*args, **kwargs)
    
    def numerator(self, *args, **kwargs):
        return _val().numerator(*args, **kwargs)
    
    def real(self, *args, **kwargs):
        return _val().real(*args, **kwargs)
    
    def to_bytes(self, *args, **kwargs):
        return _val().to_bytes(*args, **kwargs)

if __name__ == "__main__":
    Maybe = Might_Be()
    #sets Maybe to and instance of the Might_Be class.
else:
    sys.modules[__name__] = Might_Be()
    #changes the imported module object to an instance of the Might_Be class.
