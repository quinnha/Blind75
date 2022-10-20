from collections import Counter

def topKFrequent(words, k):
    
    c = Counter(words)                         
        
    ans = sorted(c, key = lambda x: (-c[x],x))  
                                                
    return ans[:k]

print(topKFrequent(["i","love","leetcode","i","love","coding"], 1))