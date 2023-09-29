class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while True:
            if n in seen:
                return False
            if n == 1 or n == 10 or n == 100 or n == 1000:
                return True
            else:
                seen.add(n)
            n = self.splitter(n)
        return False
    
    def splitter(self,n):
        curr_sum = 0
        while n != 0:
            curr_sum += (n % 10) ** 2
            n //= 10
        return curr_sum
        