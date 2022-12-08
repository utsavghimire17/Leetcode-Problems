class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        end = 1
        count = 0
        while end < len(nums):
            if nums[start] == val:
                if nums[end] == val:
                    end += 1
                    continue
                else:
                    nums[start], nums[end] = nums[end],nums[start]
                    
            start += 1
            end += 1
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop()
        return len(nums)
        