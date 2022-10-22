def maxProfit(prices) -> int:
        l, r = 0, 0
        out = 0
        while l <= r and r < len(prices):
            if prices[r] < prices[l]: 
                l = r
                r += 1
            else:
                out = max(out, prices[r] - prices[l])
                r += 1
        return out