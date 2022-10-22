
# dp[0] = 1, dp[1] = 1 + dp[0], dp[2] = 1 + dp[1], counting min num coins for any i, so work from 1 up to amount

def coinChange(coins,amount):

    dp = [amount + 1] * (amount + 1) # set array to maximum amount, this stores min no. of coins needed at any amount

    dp[0] = 0 # set base case

    for i in range(1, amount + 1): #loop through all in dp[]
        for coin in coins:
            if i-coin >= 0: #if the coin is less than the amount looked at (if its bigger, then it wont fit)
                dp[i] = min(dp[i], 1 + dp[i-coin]) # find the min of all attemps (7 - 3+4, 1+6, 2+5, etc)

    return dp[amount] if dp[amount] != amount + 1 else -1 # if there has been no change, then return -1
    


    



# print(coinChange([2,5],11))
# print(coinChange([1,21474836472],2))
print(coinChange([186,419,83,408], 6249))
