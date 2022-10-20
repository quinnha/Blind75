
from collections import defaultdict


def characterReplacement(s,k):
    l = 0

    dic = {}
    out = 0
    
    for i in set(s): dic[i] = 0

    for r in range(len(s)):
        
        dic[s[r]] += 1

        if k >=  (r - l + 1) - max(dic.values()):
            out = max(out, r-l + 1)
        else:
            dic[s[l]] -= 1
            l += 1
    return out
        


        

print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))