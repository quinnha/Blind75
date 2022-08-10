from itertools import accumulate 
import operator

def productExceptSelf (nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    # edge case
    if nums.count(0) > 1:
        return [0 for i in nums]
    elif nums.count(0) == 1:
        product = 1
        for i in range(len(nums)):
            if nums[i] != 0: 
                product *= nums[i]
            elif nums[i] == 0:
                index = i
        rlist = [0 for i in nums]
        for i in range(len(nums)):
            if i == index: rlist[i] = product 
        return rlist 

        
    product = 1

    for i in nums:
        product *= i 

    prod =  [int(product * pow(i, -1)) for i in nums]
    return prod 

