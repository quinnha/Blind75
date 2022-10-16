
def search(nums, target):

    left = 0
    right = len(nums) - 1
    
    while left <=  right:
        mid = left + (right - left)//2
        if nums[mid] == target: return mid
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1

print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))
print(search([5], 5))
print(search([2], 5))
            
