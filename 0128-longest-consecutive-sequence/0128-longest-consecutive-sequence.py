class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        curr_streak = 1
        max_streak = 0
        num_set = set()
        if len(nums) == 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i] + 1 == nums[i+1]:
                curr_streak += 1
            else:
                curr_streak = 1
            max_streak = max(curr_streak, max_streak)
        if curr_streak:
            max_streak = max(curr_streak,max_streak)
        return max_streak