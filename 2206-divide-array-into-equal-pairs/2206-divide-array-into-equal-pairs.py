class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = {}
        for i in nums:
            temp[i] = 1 + temp.get(i,0)
        for val in temp.values():
            if val % 2 != 0:
                return False
        return True