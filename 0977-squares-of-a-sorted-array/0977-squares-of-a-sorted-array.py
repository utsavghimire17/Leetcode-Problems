class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = [0] * len(nums)
        val = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] < 0:
                nums[start] = nums[start]*-1
            if nums[end] < 0:
                nums[end] = nums[end] *-1
            if nums[start] >= nums[end]:
                sorted_nums[val] = nums[start]**2
                start += 1
            elif nums[start] < nums[end]:
                sorted_nums[val] = nums[end]**2
                end -= 1
            val -= 1
        return sorted_nums
                
            