'''This is a module, preferably with the filename "Maybe.txt", so that you can just type "import Maybe" and it'll all be done: it will result in an instance of the Might_Be class stored under the name "Maybe". Alternatively, you can run the module on it's own and do your coding afterwards. That should work too.
This doesn't meet the final condition of forbidding assignment to Maybe.
Maybe behaves like a random boolean each time it is used.
e.g. "sum(Maybe for _ in range(1000))" returns approximately 500, binomially distributed.
e.g. "Maybe * 1000" returns either 1000 or 0.
Made by IFcoltransG'''

import random, sys

def _val():
    #gets the random boolean
    #used each time a method of Maybe is called, to return a different value
    return bool(random.randrange(2))
def _thorough_dir(cls):
    #creates a list of attributes a class implements
    #does not support arbitrary objects, only types
    #unlike dir(), does not sort the results
    attributes_found = []
    all_superclasses = cls.__mro__
    for superclass in all_superclasses:
        #appends the keys of __dict__ to the list
        attributes_found += superclass.__dict__
    return attributes_found


#accumulates modified versions of bool's attributes
_Maybe_class_dict = {}
for attribute_name in _thorough_dir(bool):
    if attribute_name == "__new__":
        continue
    if callable(True.__getattribute__(attribute_name)):
        def _enclose_method_name(attribute_name):
            def new_method(self, *args, **kwargs):
                return _val().__getattribute__(attribute_name)(*args, **kwargs)
            return new_method
        _Maybe_class_dict[attribute_name] = _enclose_method_name(attribute_name)
    else:
        def _enclose_attribute_name(attribute_name):
            def getter(self):
                return _val().__getattribute__(attribute_name)
        _getter = _enclose_attribute_name(attribute_name)
        _Maybe_class_dict[attribute_name] = property(_getter)

#a wrapper class for boolean attributes that delegates randomly to True or False
Might_Be = type("Might_Be", (), _Maybe_class_dict)

if __name__ == "__main__":
    Maybe = Might_Be()
    #sets Maybe to an instance of the Might_Be class.
else:
    sys.modules[__name__] = Might_Be()
    #changes the imported module object to an instance of the Might_Be class.
