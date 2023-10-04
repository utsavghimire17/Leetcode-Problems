class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if i < 0:
                if nums[-1 * i] < 0:
                    return -1 * i
                nums[-1 * i] *= -1
            else:
                if nums[i] < 0:
                    return i
                nums[i] *= -1
          