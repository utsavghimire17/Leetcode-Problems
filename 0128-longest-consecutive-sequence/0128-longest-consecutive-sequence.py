class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 1
        max_streak = 0
        nums_set = set(nums)
        for i in nums:
            if i - 1 not in nums_set:
                curr_num = i
                curr = 1
                while curr_num + 1 in nums_set:
                    curr += 1
                    curr_num = curr_num + 1
            max_streak = max(curr,max_streak)
        return max_streak