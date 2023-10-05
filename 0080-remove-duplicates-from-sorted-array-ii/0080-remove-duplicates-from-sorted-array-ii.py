class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        count = 0
        while end < len(nums):
            count = 1
            while end + 1 < len(nums) and nums[end] == nums[end+1]:
                count += 1
                end  += 1
                
            for i in range(min(2,count)):
                nums[start] = nums[end]
                start += 1
            end += 1
        return start
                
                
            
        