class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 1
        while end < len(nums):
            if nums[end] != 0:
                if nums[start] == 0:
                    nums[start],nums[end] = nums[end],nums[start]
                    start += 1
                    end += 1
                elif nums[start] != 0:
                    start += 1
                    end += 1
            else:
                if nums[start] == 0:
                    end += 1
                else:
                    start += 1
                    end += 1