import itertools
def letterCombinations(digits):
    if len(digits) == 0: return []
    maps = [[],[],["a", "b", "c"],["d", "e", "f"],["g", "h", "i"],["j", "k", "l"],["m", "n", "o"],["p", "q", "r", "s"],["t", "u", "v"],["w", "x", "y", "z"]]
    temp = list(itertools.product(*[maps[int(char)] for char in digits]))
    out = []
    for combo in temp:
        out.append(''.join(combo))
    return out

print(letterCombinations("22"))