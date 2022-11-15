class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        curr_sum = 0
        max_sum = 0
        while start < end:
            curr_sum = nums[start] + nums[end]
            if curr_sum < k:
                if curr_sum > max_sum:
                    max_sum = curr_sum
                start += 1
            elif curr_sum >= k:
                end -= 1
        if max_sum:
            return max_sum
        return -1