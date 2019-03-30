'''This is a module, preferably with the filename "Maybe.txt", so that you can just type "import Maybe" and it'll all be done: it will result in an instance of the Might_Be class stored under the name "Maybe". Alternatively, you can run the module on it's own and do your coding afterwards. That should work too.
This doesn't meet the final condition of forbidding assignment to Maybe.
Maybe behaves like a random boolean each time it is used.
e.g. "sum(Maybe for _ in range(1000))" returns approximately 500, binomially distributed.
e.g. "Maybe * 1000" returns either 1000 or 0.
Unfortunately, the interactions of "and" and "or" with Maybe may give counterintuitive results, and as such are not supported. Instead, use "bool(Maybe)", or just "&" and "|".
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
for attribute_name in set(_thorough_dir(bool)):
    if attribute_name == "__new__":
        continue
    def _enclose_method_name(attribute_name):
        def new_method(self, *args, **kwargs):
            #replace all Maybes in the function arguments with their boolean equivalents
            new_args = [arg if type(arg) is not Might_Be else bool(arg)
                        for arg in args]
            new_kwargs = {keyword: kwarg if type(kwarg) is not Might_Be else bool(kwarg)
                          for keyword, kwarg in kwargs.items()}
            return_value = _val().__getattribute__(attribute_name)(*new_args, **new_kwargs)
            #if it would return another Maybe, collapse the superposition, as it were
            if type(return_value) is Might_Be:
                return bool(return_value)
            return return_value
        return new_method
    _Maybe_class_dict[attribute_name] = _enclose_method_name(attribute_name)

#a wrapper class for boolean attributes that delegates randomly to True or False
Might_Be = type("Might_Be", (), _Maybe_class_dict)

if __name__ == "__main__":
    Maybe = Might_Be()
    #sets Maybe to an instance of the Might_Be class.
else:
    sys.modules[__name__] = Might_Be()
    #changes the imported module object to an instance of the Might_Be class.
