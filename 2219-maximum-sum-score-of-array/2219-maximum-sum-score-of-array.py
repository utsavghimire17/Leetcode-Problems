class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        max_score = float("-inf")
        max_ans = float("-inf")
        total = sum(nums)
        curr_sum = 0
        for num in nums:
            curr_sum += num
            max_score = max(curr_sum, total)
            total -= num
            max_ans = max(max_score,max_ans)
        return max_ans