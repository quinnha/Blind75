# Given a string of 1 and 0s return longest 1 substring

def sol(s):

    ans = 0
    left, right = 0, 0

    if len(s) == 1 and s[0] == "1": return 1

    while left <= right and right < len(s):

        if s[right] == "1": 
            ans = max(ans, right - left + 1)
            right += 1
        else:
            left = right
            left += 1
            right += 1
    return ans

print(sol("11011101"))
print(sol(""))
print(sol("1"))
print(sol("1111111111"))
print(sol("000000110000001"))
