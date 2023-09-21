from collections import Counter

# two sum
def twoSum(nums, target):

    dic = {}
    for i, num in enumerate(nums):
        dic[target-num] = i

    for i, num in enumerate(nums):
        if num in dic.keys() and i != dic[num]: return [i, dic[num]]

# valid anagram
def isAnagram(s, t):
    return Counter(s) == Counter(t)