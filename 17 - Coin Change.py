from itertools import count


def coinChange(coins,amount):

    if amount == 0: return 0

    coins.sort()
    n = 0

    if amount in coins:
        return 1
    else: 
        if len(coins) == 1:
            if coins[0] < amount: 
                n = coins[0]
        for i in range(len(coins)-1,-1,-1):
            if coins[-i] < amount:
                n = coins[i]
                break

    if n == 0:        
        return -1

    return 1 + coinChange(coins, amount-n)
    



print(coinChange([1,2,5],11))
print(coinChange([1,21474836472],2))
