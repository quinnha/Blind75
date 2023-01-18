# Modified String Compression 2 - https://leetcode.com/problems/string-compression-ii/description/
# Sliding Window with String Compression 1 - https://leetcode.com/problems/string-compression/description/

def solution(S, K):
    runs = len(S) - K

    min_char = float("inf")
    for run in range(runs):
        print(S.replace(S[run: run + K], ""))
        min_char = min(min_char, compress(S.replace(S[run: run + K], "")))
    return min_char


def compress(chars) -> int:
    chars = list(chars)
    walker, runner = 0, 0
    while runner < len(chars):
    
        chars[walker] = chars[runner]
        count = 1
        
        while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
            runner += 1
            count += 1
        
        if count > 1:
            for c in str(count):
                chars[walker+1] = c
                walker += 1
        
        runner += 1
        walker += 1
    
    return walker