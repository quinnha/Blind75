# best time to buy and sell stock
def maxProfit(prices):
    if len(prices) == 1:
        return 0
    max_profit = 0

    l = 0
    r = 1

    while l != len(prices) and r != len(prices):
        max_profit = max(max_profit, prices[r] - prices[l])
        if prices[l] > prices[r]:
            l += 1
        else:
            r += 1

    return max_profit
