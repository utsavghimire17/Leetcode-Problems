class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x:x[0])
        new_interval = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= new_interval[1]:
                new_interval = [min(new_interval[0],intervals[i][0]), max(new_interval[1],intervals[i][1])]
            else:
                res.append(new_interval)
                new_interval = intervals[i]
        if new_interval:
            res.append(new_interval)
        return res