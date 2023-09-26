class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, i in enumerate(temperatures):
            while stack and stack[-1][0] < i:
                res[stack[-1][1]] = idx - stack[-1][1]
                stack.pop()
                
            stack.append([i,idx])
        return res