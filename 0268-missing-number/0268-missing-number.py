class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        rslt = 0
        for i in range(len(nums)+1):
            rslt = rslt ^ i
        
        for i in nums:
            rslt = rslt ^ i
        
        return rslt
        