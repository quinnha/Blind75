

def lengthOfLongestSubstring(s):

    check = {}
    counter = 0
    m_len = 0
    
    left = 0
    right = 0
    
    while right < len(s):
        if s[right] not in check.keys():
            counter += 1
            check[s[right]] = ""
            right += 1
        else:
            check.pop(s[left])
            left += 1
            counter -= 1
        m_len = max(counter, m_len)

# print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("au"))


        

    
            
