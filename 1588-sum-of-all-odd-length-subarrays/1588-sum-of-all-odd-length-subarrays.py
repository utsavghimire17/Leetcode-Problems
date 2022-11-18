class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        curr_sum = 0
        max_sum = 0
        for i in range(len(arr)-2):
            curr_sum = 0
            for j in range(i,len(arr)):
                curr_sum += arr[j]
                if (j - i + 1) % 2 == 1:
                    max_sum += curr_sum
        return max_sum + sum(arr[len(arr)-2:])