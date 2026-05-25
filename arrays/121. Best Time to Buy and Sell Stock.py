class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        maxprofit = 0
        l = 0
        r = 1

        while r < n:
            if prices[r] - prices[l] < 0:
                l = r
                r += 1
            else:
                maxprofit = max(maxprofit, prices[r] - prices[l])
                r += 1

        return maxprofit
        