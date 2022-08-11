
def search (nums, target):

    left = 0
    right = len(nums) -1

    if len(nums) == 1 and nums[0] == target: return 0
    elif len(nums) == 1 and nums[0] != target: return -1


    while left < right:

        middle = left + (right - left) // 2

        # acceptence criteria
        if nums[middle] == target: return middle
        
        # move left/right criteria
        if nums[middle] >= nums[left]: #left side is increasing
            if target < nums[middle] and target >= nums[left]: #check if number is in the range
                right = middle - 1 #move left
            else: 
                left = middle + 1 # move right

        else: #right side increasing
            if target > nums[middle] and target <= nums[right]: #check if number is in the range
                left  = middle + 1 #move right
            else: 
                right = middle - 1 # move left

    


    # if the loop existed and no return, that means low crossed high (middle)
    return left if (nums[left] == target) else -1

# print(search([4,5,6,7,8,1,2,3],8))
# print(search([4,5,6,7,0,1,2],3))
# print(search([1,2],3))
print(search([1,3],3))

# a = [1,2,3]
# print(len(a[1:2])) #1