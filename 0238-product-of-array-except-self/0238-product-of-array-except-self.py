class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        postfix = 1
        res = []
        for i in nums:
            res.append(prefix)
            prefix *= i
        
        for i in range(len(res)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res