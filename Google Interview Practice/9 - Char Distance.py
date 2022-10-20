from collections import Counter, defaultdict
from typing import Dict

def sol(keyboard, s):

    dist = {}

    for i in range(len(keyboard)):
        dist[keyboard[i]] = i
    
    out = 0
    temp = 0

    for char in s:
        out += abs(dist[char] - temp)
        temp = dist[char]
    
    return out


print(sol("abcdefghijklmnopqrstuvwxy", "cba"))