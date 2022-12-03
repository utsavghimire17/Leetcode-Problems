class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        
        start = 0
        end = 0
        curr_sum = 0
        max_avg = float("-inf")
        while end < len(nums):
            curr_sum += nums[end]
            if (end - start + 1) < k:
                end += 1
            elif (end - start + 1) == k:
                max_avg = max(max_avg, (curr_sum)/k)
                end += 1
                curr_sum -= nums[start]
                start += 1
        return (max_avg)