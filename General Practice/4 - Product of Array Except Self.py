from itertools import accumulate 
import operator

# def productExceptSelf (nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
    
#     # edge case
#     if nums.count(0) > 1:
#         return [0 for i in nums]
#     elif nums.count(0) == 1:
#         product = 1
#         for i in range(len(nums)):
#             if nums[i] != 0: 
#                 product *= nums[i]
#             elif nums[i] == 0:
#                 index = i
#         rlist = [0 for i in nums]
#         for i in range(len(nums)):
#             if i == index: rlist[i] = product 
#         return rlist 

        
#     product = 1

#     for i in nums:
#         product *= i 

#     prod =  [int(product * pow(i, -1)) for i in nums]
#     return prod 

# Better Sol -> calculate left prof and right prod
# This solution uses the fact that you can keep track of the product on the left side
# and the right side in 1 loop each, and then when you multiply them together, you get
# the product of array except self (math is neat)

def productExceptSelf (nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    res = [1 for i in nums]
    res1 = [1 for i in nums]
    left = right =1
    #get left
    for i in range (1, len(nums)):
        left *= nums[i-1]
        res[i] = left 
    #get right - limit to -1 to cover the 0th element
    for i in range (len(nums)-1, -1, -1):
        if (i < len(nums)-1): 
            right *= nums[i+1]
        res[i] *= right 
    return res 

print (productExceptSelf([2,3,4,5]))