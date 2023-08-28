class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current_streak = 0
        consecutive = set(nums)
        longest_streak = 0
        for num in nums:
            if num -1 not in consecutive:
                current = num
                current_streak = 1
                
                while current + 1 in consecutive:
                    current_streak += 1
                    current += 1
                
            longest_streak = max(longest_streak,current_streak)
        return longest_streak