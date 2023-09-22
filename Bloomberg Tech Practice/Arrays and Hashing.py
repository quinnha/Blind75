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


# product except self
def productExceptSelf(nums):
    ret = [1] * len(nums)

    # left
    t = 1
    for i, num in enumerate(nums):
        ret[i] *= t
        t *= num

    # right
    t = 1
    for i, num in enumerate(nums[::-1]):
        ret[len(nums) - i - 1] *= t
        t *= num

    return ret


# longest consecutive sequence
def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in nums:
        j, curr_longest = 1, 1
        # look left
        while num - j in num_set:
            num_set.remove(num - j)
            j += 1
            curr_longest += 1
        j = 1
        # look right
        while num + j in num_set:
            num_set.remove(num + j)
            j += 1
            curr_longest += 1
        longest = max(longest, curr_longest)

    return longest


print(longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
print(longestConsecutive([0, -1]))
