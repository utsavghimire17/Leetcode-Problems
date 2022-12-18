class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        index = {}
        for i in range(len(nums2)):
            index[nums2[i]] = i
        for j in nums1:
            val = False
            for k in range(index[j] + 1,len(nums2)):
                if nums2[k] > j:
                    val = True
                    res.append(nums2[k])
                    break
            if not val: 
                res.append(-1)
        return res