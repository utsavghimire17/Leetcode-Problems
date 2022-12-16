class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start = 0
        end = 1
        count = 0
        while end < len(nums):
            if nums[end] > nums[start]:
                start = end 
                end += 1
            elif nums[end] <= nums[start]:
                count += 1
                if start < 1:
                    start = end
                    end += 1
                    continue
                
                if nums[end] <= nums[start - 1]:
                    end += 1
                elif nums[end] > nums[start - 1]:
                    start = end 
                    end += 1
        if count >= 2:
            return False
        return True