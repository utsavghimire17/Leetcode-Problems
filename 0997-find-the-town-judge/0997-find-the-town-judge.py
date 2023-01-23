class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
      
        count = [0] * n
        for i in trust:
            count[i[1] - 1] += 1
            count[i[0] - 1] -= 1
        for idx in range(len(count)):
            if count[idx] == n - 1:
                return idx + 1
        return -1