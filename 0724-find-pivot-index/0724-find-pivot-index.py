class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_nums = []
        postfix_nums = [0] * len(nums)
        prefix = 0
        postfix = 0
        for i in nums:
            prefix_nums.append(prefix)
            prefix += i
        for i in range(len(nums) -1 , -1,-1):
            postfix_nums[i] = postfix
            postfix += nums[i]
        for idx in range(len(nums)):
            if prefix_nums[idx] == postfix_nums[idx]:
                return idx
            
        return -1
        
        