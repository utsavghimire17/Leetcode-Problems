class Solution(object):
    def sumZero(self, n):
        res = []
        if n % 2 == 0:
            for i in range(n/2 + 1):
                if i > 0:
                    res.append(-1 * i)
                    res.append(i)
        else:
            for i in range(n/2 + 1):
                res.append(i)
                if i > 0:
                    res.append(-1 * i)
        return res
                
        