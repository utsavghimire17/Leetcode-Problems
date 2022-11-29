class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_num = nums[0]
        count = 0
        max_count = float('-inf')
        for num in nums:
            if num == curr_num:
                count += 1
            else:
                count -= 1
            if count == 0:
                curr_num = num
                count = 1
            if count >= max_count:
                max_count = count
                curr_num = num
        return curr_num