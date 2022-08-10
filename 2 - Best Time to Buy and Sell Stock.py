# if buy pointer > sell pointer (lose money) set buy to sell
# if not, if diff is larger than max, set max
# no matter what, move sell pointer one to the right


from regex import D

def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        buy = 0
        sell = 0
        for i in range (len(prices)):
            if prices[buy] > prices[sell]: 
                buy = sell
            else:
                if prices[sell] - prices[buy] > max:
                    max = prices[sell] - prices[buy]
            sell += 1
        return max


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([2,4,1,9]))