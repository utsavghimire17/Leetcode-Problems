class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        last = -1
        first_occur = False
        for i in range(len(nums)):
            if nums[i] == target:
                if first_occur == False:
                    first = i
                    first_occur = True
                if first_occur == True:
                    last = i
        return [first,last]