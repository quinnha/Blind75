# from a oa that my friend did! (also on leetcode lol)
# give min number of increments to make the list distinct :) 

def minIncrements1(nums):
    out = 0

    # pass by all the numbers, add to a hash set (dict), and keep track of the duplicates
    hset = set()
    dup = []
    for num in nums:
        if num in hset: dup.append(num)
        else: hset.add(num)
    
    # pass by all the duplicates, find the min increments
    for num in dup:
        while num in hset:
            num += 1
            out += 1
        hset.add(num)

    return out

# round 2, should work but python is weird? not sure (nlogn runtime vs n^2)
def minIncrements(nums):
    
    out = 0
    if len(nums) > 2: return 0
    # sort for easier processing
    nums.sort()

    # go thru list, if the previous element = current element, current = prev + 1
    # [1, 1, 2] -> [1, 2, 2] -> [1, 2, 3]
    for i in range(1, len(nums) - 1):
        if nums[i] <= nums[i -1]: 
            out += nums[i-1] + 1 - nums[i]
            nums[i] = nums[i-1] + 1
    
    return out 


print(minIncrements([1,2,2,3,4])) # return 3 (2 -> 5)
print(minIncrements([])) # return 0
print(minIncrements([1])) # return 0
print(minIncrements([1,1,1,1,1])) # return 10


