class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        curr_sum = 0
        min_path = float('inf')
        while end < len(nums):
            curr_sum += nums[end]
            while curr_sum >= target:
                min_path = min(min_path, end- start + 1)
                curr_sum -= nums[start]
                start += 1
            end += 1
        if min_path == float("inf"):
            return 0
        return min_path