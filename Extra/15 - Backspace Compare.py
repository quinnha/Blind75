def backspaceCompare(self, s: str, t: str) -> bool:
    s1 = ""
    t1 = ""
    for char in s:
        
        if char == "#": s1 = s1[:-1]
        else: s1 += char

    for char in t:
        if char != "#": t1 += (char)
        else: t1 = t1[:-1]

    return s1 == t1