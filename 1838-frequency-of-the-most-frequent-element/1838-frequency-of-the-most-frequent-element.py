class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = 0
        curr_sum = 0
        max_freq = 1
        while end < len(nums):
            while end < len(nums) and (end - start) * nums[end] <= curr_sum + k:
               curr_sum += nums[end]
               end += 1
            max_freq = max(max_freq, end - start)
            curr_sum -= nums[start]
            start += 1
        print(nums)
        return max_freq