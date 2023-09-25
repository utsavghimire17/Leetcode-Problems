class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search_right(nums,target):
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    if mid + 1 == len(nums) or nums[mid+1] != target:
                        return mid
                    else:
                        start = mid + 1
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
            return -1
        
        def binary_search_left(nums,target):
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    if mid - 1 == -1 or nums[mid-1] != target:
                        return mid
                    else:
                        end = mid - 1
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
            return -1 
        start_index = binary_search_left(nums,target)
        end_index = binary_search_right(nums,target)
        return [start_index, end_index]