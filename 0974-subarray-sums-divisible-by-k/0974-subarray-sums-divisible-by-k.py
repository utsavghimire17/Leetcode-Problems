class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        curr_sum = 0
        temp = {0 : 1}
        for i in nums:
            curr_sum += i
            rem = curr_sum % k
            if rem in temp:
                res += temp[rem]
            temp[rem] = 1 + temp.get(rem,0)
        return res
                    