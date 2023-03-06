class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell = 0
        max_profit = -1
        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
        return max_profit