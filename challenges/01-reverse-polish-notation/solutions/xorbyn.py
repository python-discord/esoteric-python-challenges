"""
Submission by Xorbyn
"""

IN = '15 7 1 1 + − ÷ 3 × 2 1 1 + + −'
#    ((15 ÷ (7 − (1 + 1))) × 3) − (2 + (1 + 1))

operators = {
    '+': lambda n1, n2: n1 + n2,
    '−': lambda n1, n2: n1 - n2,
    '÷': lambda n1, n2: n1 / n2,
    '×': lambda n1, n2: n1 * n2
}

def isint(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True


def evaluate(s):

    def update_stack(stack, mem):
        if isint(mem):
            stack = (*stack, int(mem))
        else:
            n1, n2 = stack[-2:]
            stack = stack[:-2]
            stack = (*stack, operators[mem](n1, n2))

        return stack

    stack = tuple()
    mem = ''
    for char in s:
        if char == ' ':
            stack = update_stack(stack, mem)
            mem = ''
        else:
            mem += char

    return update_stack(stack, mem)[0]






print(evaluate(IN))
