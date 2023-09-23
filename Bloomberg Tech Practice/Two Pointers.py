# is palindrome
def isPalindrome(s):
    parsed = "".join(x.lower() for x in s if x.isalnum())

    # easy way
    # return parsed == parsed[::-1]

    left = 0
    right = len(parsed) - 1

    while left < right:
        if parsed[left] != parsed[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome("0P"))
