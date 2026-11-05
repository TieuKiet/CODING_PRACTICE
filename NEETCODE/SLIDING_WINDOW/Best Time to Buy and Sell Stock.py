class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        a= [prices[0]]
        n= len(prices)
        for i in range(1, n):
            if prices[i] > a[0]:
                max_profit = max(max_profit, prices[i] - a[0])
            
            elif prices[i] < a[0]:
                a = [prices[i]]
        
        return max_profit
