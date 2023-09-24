# valid parenthesis
def isValid(s):
    stack = []
    left = ("{", "(", "[")
    right = ("}", ")", "]")
    m = {"}": "{", ")": "(", "]": "["}
    for c in s:
        if c in left:
            stack.append(c)
        elif c in right:
            if len(stack) == 0:
                return False
            if m[c] != stack[-1]:
                return False
            else:
                stack.pop(-1)
        else:
            continue
    return True if len(stack) == 0 else False
