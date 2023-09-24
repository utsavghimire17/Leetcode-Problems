class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_point = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                break_point = i
                break
        if break_point == -1:
            nums.reverse()
            return
        for j in range(len(nums)-1,break_point,-1):
            if nums[j] > nums[break_point]:
                nums[break_point], nums[j] = nums[j], nums[break_point]
                break
        start = break_point + 1
        end = len(nums) - 1
        while start < end:
            nums[start],nums[end] = nums[end], nums[start]
            start += 1
            end -= 1