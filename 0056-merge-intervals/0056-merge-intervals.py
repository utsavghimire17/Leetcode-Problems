class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        res = []
        temp = sorted_intervals[0]
        i =1 
        while i < len(sorted_intervals):
            if temp[1] >= sorted_intervals[i][0]:
                if temp[1] >= sorted_intervals[i][1]:
                    temp = [temp[0],temp[1]]
                else:
                    temp = [temp[0],sorted_intervals[i][1]]
            else:
                res.append(temp)
                temp = sorted_intervals[i]
            i += 1
        if temp:
            res.append(temp)
        return res