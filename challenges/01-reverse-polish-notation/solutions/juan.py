"""
Submission by juan (kingdom5500)
"""

reverse_polish = lambda expression: ((lambda PolishStack, split: ((lambda stack: tuple(stack.push(float(item)) if item.isdigit() else stack.operate(item) for item in split(expression)) and stack.pop())(stack=PolishStack())))(PolishStack = type("Stack", (), {"__init__": lambda self: (setattr(self, "_tuple", ())), "push": lambda self, item: (setattr(self, "_tuple", (item, *self._tuple))), "pop": lambda self: ((lambda tmp: tmp.add(self._tuple[0] if self._tuple else None) or setattr(self, "_tuple", self._tuple[1:]) or tmp.pop())(set())), "operate": lambda self, operator: ((lambda operation: self.push(operation(*(self.pop(), self.pop())[::-1])))(operation = {"+": float.__add__, "-": float.__sub__, "/": float.__truediv__, "*": float.__mul__, "^": float.__pow__}[operator]))}), split = lambda string: ((lambda spaces: (string[start:end - 1] for start, end in zip((0, *spaces), (*spaces, len(string) + 1))))(spaces = tuple(index + 1 for index, char in enumerate(string) if char.isspace())))))

"""
Annotated version

reverse_polish = lambda expression: (
    # Below is a function that is given some handy stuff
    # through its parameters, such as an entire Stack class.
    (lambda PolishStack, split: (
        (lambda stack: 
            tuple(
                stack.push(float(item)) if item.isdigit() else stack.operate(item)
                for item in split(expression)
            ) and stack.pop()
        )(stack=PolishStack())
    ))(
        # This is a basic Stack class that uses tuples internally
        PolishStack = type(
            "Stack", (), {

                # Regular __init__ method for the class.
                "__init__": lambda self: (
                    # Create an empty tuple for the stack.
                    setattr(
                        self,
                        "_tuple",
                        ()
                    )
                ),

                # "Push" an item onto the stack.
                "push": lambda self, item: (
                    # Replace the old tuple with the new one.
                    setattr(
                        self,
                        "_tuple",
                        (item, *self._tuple)
                    )
                ),

                # "Pop" an item from the stack.
                "pop": lambda self: (

                    # A util to make sure we don't lose the top
                    # item of the stack when popping it off.
                    (lambda tmp:

                        # Store the top value temporarily.
                        # Default to None if empty.
                        tmp.add(
                            self._tuple[0] if self._tuple else None
                        ) or

                        # Then, we can update the stack itself.
                        setattr(
                            self,
                            "_tuple",
                            self._tuple[1:]
                        ) or

                        # Finally, retrieve the value and return it.
                        tmp.pop()

                    # Pass an empty set to use as temporary storage.
                    )(set())
                ),

                # Perform an arithmetic operation on the top two items.
                "operate": lambda self, operator: (
                    (lambda operation:
                        # Execute the function with reversed operands,
                        # then add the result back onto the stack.
                        self.push(
                            operation(*(self.pop(), self.pop())[::-1])
                        )
                    )(
                        # Choose the corresponding function to operate.
                        operation = {
                            "+": float.__add__,
                            "-": float.__sub__,
                            "/": float.__truediv__,
                            "*": float.__mul__,
                            "^": float.__pow__
                        }[operator]
                    )
                )
            }
        ),
        
        # A generator to yield every chunk of a string, separated by spaces.
        split = lambda string: (

            # A utility function for easy access to the tuple of indices.
            (lambda spaces: (
                # Yield every chunk between all the spaces in the string.
                string[start:end - 1] for start, end in
                zip((0, *spaces), (*spaces, len(string) + 1))
            ))(
                # Construct a tuple of all indices of the whitespace.
                # It is then passed to the above function.
                spaces = tuple(
                    index + 1 for index, char in
                    enumerate(string) if char.isspace()
                )
            )
        )
    )
)
"""
