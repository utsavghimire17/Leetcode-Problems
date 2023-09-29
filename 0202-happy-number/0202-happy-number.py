class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(10):
            n = self.splitter(n)
            print(n)
            if n == 1 or n == 10 or n == 100 or n == 1000:
                return True
        return False
    
    def splitter(self,n):
        curr_sum = 0
        while n != 0:
            curr_sum += (n % 10) ** 2
            n //= 10
        return curr_sum
        