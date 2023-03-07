class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        product = 1
        count = 0
        while end < len(nums):
            product *= nums[end]
            while start <= end and product >= k:
                product /= nums[start]
                start += 1
            count += end - start + 1
            end += 1
        return count