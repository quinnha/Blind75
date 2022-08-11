# two pointer twosum for sorted array
# have pointer at beginnign and end, move em together
def twoSum (nums, target):
    left = 0
    right = len(nums)-1 

    while left <= right:
            if nums[left] + nums[right] > target:
                right-= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else: return [left+1, right+1]

    return -1


print (twoSum([2,7,11,15], 9)) 