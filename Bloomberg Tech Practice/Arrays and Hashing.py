from collections import *
from heapq import *


# two sum
def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        dic[target - num] = i

    for i, num in enumerate(nums):
        if num in dic.keys() and i != dic[num]:
            return [i, dic[num]]


# valid anagram
def isAnagram(s, t):
    return Counter(s) == Counter(t)


# contains duplicate
def containsDuplicate(nums):
    numbers = Counter(nums)

    for num in numbers:
        if numbers[num] != 1:
            return True
    return False


# group anagrams
def groupAnagrams(strs):
    sort = defaultdict(list)

    for s in strs:
        sort["".join(sorted(s))].append(s)

    return [sort[key] for key in sort.keys()]


# top k frequent -> remember that heaps are minheaps
def topKFrequent(nums, k):
    count = Counter(nums)

    heap = []
    for key in count.keys():
        heappush(heap, (count[key] * -1, key))

    print(count)
    print(heap)

    ret = []

    for i in range(k):
        ret.append(heappop(heap)[1])

    return ret
