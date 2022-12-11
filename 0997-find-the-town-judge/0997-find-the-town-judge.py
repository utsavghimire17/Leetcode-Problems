class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
      
        temp = {}
        ignore = set()
        if len(trust) == 0:
            if n%2 == 0:
                return -1
            return 1
        for i in range(len(trust)):
            temp[trust[i][1]] = []
        for i in range(len(trust)):
            if trust[i][0] in temp:
                ignore.add(trust[i][0])
            temp[trust[i][1]].append(trust[i][0])
        for cand in temp:
            if len(temp[cand]) == n-1 and cand not in ignore:
                return cand
        return -1