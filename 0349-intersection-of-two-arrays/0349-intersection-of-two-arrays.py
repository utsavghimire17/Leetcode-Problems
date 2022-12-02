class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = set(nums1)
        res = []
        for i in nums2:
            if i in temp:
                res.append(i)
                temp.remove(i)
        return res