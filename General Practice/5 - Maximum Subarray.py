# Basically count sum, if the sum is negative, reset the count at the new index
# and store the max sum!

def maxSubArray(nums):

    maxi = nums[0]
    sum = 0
    for i in nums:
        if sum < 0:
            sum = 0
        sum += i
        maxi = max(maxi, sum)
    return maxi 

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([-2,-1,-3,-5,-3,-10]))


