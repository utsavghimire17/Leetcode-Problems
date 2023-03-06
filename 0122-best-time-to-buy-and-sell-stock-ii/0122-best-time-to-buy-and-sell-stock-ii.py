class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy = 0
        for sell in range(1,len(prices)):
            if prices[sell] > prices[buy]:
                max_profit += prices[sell] - prices[buy]
            buy += 1
        return max_profit
        