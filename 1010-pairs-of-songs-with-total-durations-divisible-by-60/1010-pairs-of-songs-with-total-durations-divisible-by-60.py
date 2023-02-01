class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        temp = {}
        count = 0
        for i in time:
            if (60 - (i % 60))% 60 in temp:
                count += temp[(60 - (i % 60))% 60]
            if i % 60 in temp:
                temp[i % 60] += 1
            else:
                
                temp[i % 60] = 1
        return count