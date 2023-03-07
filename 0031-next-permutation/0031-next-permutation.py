class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        break_index = -1
        while i >= 0:
            if nums[i] < nums[i+1]:
                break_index = i
                break
            i -= 1
        if break_index == -1:
            return nums.reverse()
        for j in range(len(nums)-1,-1,-1):
            if nums[j] > nums[break_index]:
                nums[j],nums[break_index] = nums[break_index],nums[j]
                break
                
        start = break_index + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
        