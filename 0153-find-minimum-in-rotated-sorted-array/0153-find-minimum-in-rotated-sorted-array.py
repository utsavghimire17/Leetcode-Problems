class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if len(nums) == 0:
            return nums[0]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[start] <= nums[end]:
                return nums[start]
            if nums[mid] >= nums[start]:
                start = mid + 1
            elif nums[mid] < nums[start]:
                end = mid - 1
        return nums[start]