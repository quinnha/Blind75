from collections import Counter


# best time to buy and sell stock
def maxProfit(prices):
    if len(prices) == 1:
        return 0
    max_profit = 0

    l = 0
    r = 1

    while l != len(prices) and r != len(prices):
        max_profit = max(max_profit, prices[r] - prices[l])
        if prices[l] > prices[r]:
            l += 1
        else:
            r += 1

    return max_profit


# longest unique substring
def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        return 2 if s[0] != s[1] else 1

    l = 0
    r = 0

    seen = set()
    max_len = 0

    while l != len(s) and r != len(s):
        if s[r] not in seen:
            seen.add(s[r])
            r += 1
            max_len = max(max_len, r - l)
        else:
            seen.remove(s[l])
            l += 1

    return max_len


# longest repeating character (incorrect)
def characterReplacement(self, s: str, k: int) -> int:
    l, r = 0, 1
    max_len = 0

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    while l != len(s) and r != len(s):
        count = Counter(s[l:r])
        maxf = max(count.values())

        if r - l + 1 <= k or maxf + k >= r - l:
            max_len = max(max_len, r - l + 1)
            print(s[l:r], count, max_len)
            r += 1
        else:
            l += 1
    return max_len
