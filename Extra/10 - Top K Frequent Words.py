from collections import Counter

# counter is a bit weird, maybe avoid? can also use a heap lol
def topKFrequent(words, k):
    
    c = Counter(words)
        
    ans = sorted(c, key = lambda x: (-c[x],x))  
                                                
    return ans[:k]

(topKFrequent(["i","love","leetcode","i","love","coding"], 1))