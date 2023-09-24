class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] >= nums[start]:
                if nums[end] < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                end = mid - 1
             
        return nums[mid]