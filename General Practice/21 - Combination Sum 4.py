# target = num1 + num2 -> dp[target] = dp[num1] +dp[num2] for all num1 in num
def combinationSum4(nums, target):

    dp = [0] * (target + 1) # store number of combos from 0-targer

    for i in range(len(dp)):
        for num in nums:
            if num < i:
                dp[i] = dp[i] + dp[(i-num)] 
            elif num == i:
                dp[i] += 1

    return dp[-1]

print(combinationSum4([1,2,3], 4))