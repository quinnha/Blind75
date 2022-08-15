
# idea is to have a array to chacks how many numbers on left hand are less than index, and take max!
def lengthOfLIS(nums):

    dp =[1] * len(nums)
    if len(nums) <= 1: return len(nums) # base case

    for i in range(1, len(nums)): # start at 1 so you can compare 0th element
        for j in range(0, i):
            # if the number at left pointer is smaller, and 1+ left pointer is larger than right pointer, take max
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]: dp[i] = dp[j] + 1
    return max(dp)

print(lengthOfLIS([1,2,3]))
print(lengthOfLIS([10,9,2,5,3,7,101,18]))

a = [1,2,3,4,5]
print(len(a))