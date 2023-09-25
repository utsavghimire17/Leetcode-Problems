class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        count = 1
        max_count = 0
        seen = set()
        for i in nums:
            if i - 1 not in nums_set:
                curr = i
                count = 1
                while curr + 1 in nums_set:
                    curr = curr + 1
                    count += 1
            max_count = max(count,max_count)
        return max_count