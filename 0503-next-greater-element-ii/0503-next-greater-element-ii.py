class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        for idx in range(len(nums)):
            while stack and nums[idx] > stack[-1][0]:
                res[stack[-1][1]] = nums[idx]
                stack.pop()
            stack.append([nums[idx],idx])
        if stack:
            for idx in range(len(nums)):
                while stack and nums[idx] > stack[-1][0]:
                    res[stack[-1][1]] = nums[idx]
                    stack.pop()
        return res