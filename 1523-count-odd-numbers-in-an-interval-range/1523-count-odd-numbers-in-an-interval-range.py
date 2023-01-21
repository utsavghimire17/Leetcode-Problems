from math import ceil
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        if low % 2 == 1 and high % 2 == 0 or (low % 2 == 0 and high % 2 == 1):
            return ceil((high - low) / 2)
        if low % 2 == 1 and high % 2 == 1:
            return ((high-low) // 2) + 1
        