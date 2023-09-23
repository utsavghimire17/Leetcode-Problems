class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        max_profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
            elif prices[sell] <= prices[buy]:
                buy = sell
            sell += 1
            max_profit = max(max_profit, profit)
            
        return max_profit
       