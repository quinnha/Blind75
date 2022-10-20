
from collections import defaultdict

from collections import defaultdict

# TLE, too many passes lol
def minDominoRotations(tops, bottoms):

    if len(tops) == 0: return 0
    if len(tops) != len(bottoms): return -1
    
    top_count = defaultdict(int)
    bot_count = defaultdict(int)
    count = defaultdict(int)
    out = 0

    for i in range(len(tops)):
        top_count[tops[i]] += 1
        bot_count[bottoms[i]] += 1
        count[tops[i]] += 1
        count[bottoms[i]] += 1

    if max(count.values()) < len(tops):
        return -1
    if max(top_count.values()) == len(tops) or max(bot_count.values()) == len(bottoms): return 0
    
    val = max(count, key=count.get)

    if top_count[val] >= bot_count[val]:
        for i in range(len(tops)):
            if bottoms[i] == val and tops[i] != val:
                out += 1
                tops[i] = val
    else:
        for i in range(len(bottoms)):
            if tops[i] == val and bottoms[i] != val:
                out += 1
                bottoms[i] = val

    if tops.count(val) == len(tops) or bottoms.count(val) == len(bottoms): 
        return out
    else: 
        return -1

from collections import Counter

# better
def minDominoRotations(tops, bottoms):
    A = tops
    B = bottoms
    if len(A) != len(B): return -1
    same, countA, countB = Counter(), Counter(A), Counter(B)
    for a, b in zip(A, B):
        if a == b:
            same[a] += 1
    for i in range(1, 7):
        if countA[i] + countB[i] - same[i] == len(A):
            return min(countA[i], countB[i]) - same[i]        
    return -1



top = [1,0,1,0]
bot = [0,1,1,1]

print(minDominoRotations(top, bot))
# print(minDominoRotations([], []))
# print(minDominoRotations([1], []))
# print(minDominoRotations([1,2,1,1,3,4,5], [1,2,1,1,1,1,1]))
# print(minDominoRotations([1,2,1,1,3,4,5], [1,1,1,1,1,1,1]))
# print(minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))
# print(minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))

