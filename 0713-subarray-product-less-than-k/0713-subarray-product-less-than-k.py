class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0
        prod = 1
        count = 0
        while end < len(nums):
            prod *= nums[end]
            while end > start and start < len(nums) and prod >= k:
                prod /= nums[start]
                start += 1
            if end >= start and prod < k:
                count += end - start + 1
            end += 1
        return count