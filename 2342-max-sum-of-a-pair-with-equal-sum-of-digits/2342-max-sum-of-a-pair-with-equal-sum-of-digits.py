class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res =[]
        equal_pair = {}
        max_sum = -1
        for num in nums:
            curr_sum = 0
           
            for string in str(num):
                curr_sum += int(string)
            if curr_sum in equal_pair:
                heapq.heappush(equal_pair[curr_sum], -int(num))
            else:
                equal_pair[curr_sum] = [-num]
            curr_string = ""
        
        for pairs in equal_pair:
            curr_sum = -2
            if len(equal_pair[pairs]) >= 2:
                sum1 = -1 * heapq.heappop(equal_pair[pairs])
                sum2 = -1 * heapq.heappop(equal_pair[pairs])
                curr_sum = sum1 + sum2
            
            max_sum = max(max_sum, curr_sum)
        return max_sum
    