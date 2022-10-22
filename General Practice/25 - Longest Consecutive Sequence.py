
# can i hash all the numbers and then number + 1?
# i can check the keys, then pop after ive checked em?

from pydoc import doc


def longestConsecutive(nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best



print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longestConsecutive([0]))
print(longestConsecutive([]))
print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))

# d = {}
# d[0] = 1
# d.pop(0)

# print(d)