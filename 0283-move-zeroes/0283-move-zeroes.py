class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 0
        while end < len(nums):
            if nums[end] != 0:
                nums[start],nums[end] = nums[end], nums[start]
                start += 1
            end += 1
        