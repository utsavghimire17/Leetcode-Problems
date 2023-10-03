class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2 
            if mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
                start = mid + 1
            else:
                end = mid
        return end