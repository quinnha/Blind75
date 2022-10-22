#def took me too long for somethign so elementary
# acceptence criteria is if min is on left or right, can check 
# else move you left/right to middle, use formula below instead of being stupid
def findMin (nums):

    left = 0
    right = len(nums)-1

    if len(nums) == 1: return nums[0]
    if nums[0] < nums[right]: return nums[0]

    while True:
        
        mid = int(left + (right - left)/2)

        if nums[mid] > nums[mid+1]: return nums[mid+1]
        if nums[mid-1] > nums[mid]: return nums[mid]

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid -1
        
        



    
print (findMin ([2,3,4,5,1]))
        

        

# print (findMin ([3,4,5,1,2]))
# print (findMin ([4,5,1,2,3]))

# print (findMin ([4,5,6,7,0,1,2]))
# print (findMin ([11,13,14,17]))
# print(findMin([0]))
# print(findMin([2,1]))


