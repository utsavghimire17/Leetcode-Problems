class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        flips = 0
        ones = 0
        for char in s:
            if char == "1":
                ones += 1
            else:
                if ones > 0:
                    flips += 1
                    ones -= 1
        return flips
        