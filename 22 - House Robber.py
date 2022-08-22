# check i vs i-1 + i+1 !

def rob (nums):

    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]

    for i in range(1, len(nums)):
        val = nums[i]
        dp[i+1] = max(dp[i], dp[i-1] + val)    


    return dp[-1]