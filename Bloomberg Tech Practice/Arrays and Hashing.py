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

# contains duplicate
def containsDuplicate(nums):
    
    numbers = Counter(nums)
    
    for num in numbers:
        if numbers[num] != 1: return True
    return False
    