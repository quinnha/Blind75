
def isPalindrome(s):

    s = "".join (item for item in s if item.isalnum())
    s = s.upper()
    left = 0
    right = len(s)-1
    
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else: return "false"
    
    return "true"

print(isPalindrome("0P"))