class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                res_index = stack.pop()[0]
                res[res_index] = index - res_index
            stack.append([index,temp])
        return res