
# n^3 sadge
def longestPalindrome1(s):

    if len(s) == 0: return ""
    elif len(s) == 1: return s
    if len(s) == 2:
        if s[0] == s[1]: return s
        else: return s[1]

    m = 0
    out = ""

    for i in range(len(s)):
        sub = ""
        for j in range(i, len(s)):
            sub += s[j]

            if sub == sub [::-1]: 
                
                if len(sub) >= m:
                    out = sub
                    m = len(sub)
    return out

# n^2 weeeeee
def longestPalindrome(s):
    
    n = len(s)

    out = ""
    m = 0

    for i in range(n):
        
        right = i
        while right < n and s[i] == s[right]:
            right += 1
        
        left = i - 1
        while left >= 0 and right < n and s[left] == s[right]:
            right += 1
            left -= 1


        temp = right - left
        if temp > m:
            m = temp
            out = s[left + 1:right]
            
    return out



print(longestPalindrome("cbbd"))

