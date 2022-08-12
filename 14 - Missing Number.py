# if u xor a and b and b you get a -> so you xor the array with its indexes to see what is left

def missingNumber(nums):

    result = 0

    for pointer , value in enumerate(nums):

        result ^= (pointer +1) ^ value

    return result 



    # easy non-bit solution! (but this isnt the point of the exercise lol)
    # if len(nums) == 1 and nums[0] == 1:
    #     return 0
    # elif len(nums) == 1 and nums[0] == 0:
    #     return 1
    # for i in range(1, len(nums)+1):
    #     if nums.count(i) != 1: return i
    # return 0 
    return 0

# print(missingNumber([3,0,1]))
# print(missingNumber([9,6,4,2,3,5,7,0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))