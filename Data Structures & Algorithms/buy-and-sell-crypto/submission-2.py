class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        
        for price in prices:
            profit = max(price - lowest, profit)
            lowest = min(lowest, price)
        
        return profit