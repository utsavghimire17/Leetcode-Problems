class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        total1 = 0
        if total == nums[0]:
            return 0
        for index in range(len(nums)-1):
            total1 += nums[index]
            if total - nums[index+1] == 2*total1:
                return index+1
            
        return -1