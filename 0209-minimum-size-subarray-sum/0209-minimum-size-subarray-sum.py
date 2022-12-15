class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        curr_sum = 0
        res = float("inf")
        while end < len(nums):
            curr_sum += nums[end]
            if curr_sum >= target:
                res = min(res, end - start + 1)
                curr_sum -= nums[start]
                curr_sum -= nums[end]
                start += 1
            else:
                end += 1
        if res == float("inf"):
            return 0
        return res