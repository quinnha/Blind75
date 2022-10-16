
def isValid(s):

    stack = []

    open = ["(", "{", "["]
    close = [")", "}", "]"]

    for ch in s:
        if ch in open: stack.append(ch)
        else:
            if len(stack) == 0: return False
            if open.index(stack[-1]) == close.index(ch):
                stack = stack[:-1]
            else:
                return False
    if len(stack) > 0: return False

    return True

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))