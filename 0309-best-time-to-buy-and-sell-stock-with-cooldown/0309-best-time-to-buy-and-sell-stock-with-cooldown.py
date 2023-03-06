class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        buy = [0] * n
        sell = [0] * n
        cool = [0] * n
        buy[0] = -prices[0]

        for i in range(1, n):
            buy[i] = max(cool[i - 1] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            cool[i] = max(sell[i - 1], cool[i - 1])

        return max(sell[-1], cool[-1])
