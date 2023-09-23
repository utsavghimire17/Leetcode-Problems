class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        new_interval = intervals[0]
        for idx in range(1,len(intervals)):
            if new_interval[1] >= intervals[idx][0]:
                if new_interval[1] >= intervals[idx][1]:
                    new_interval = [new_interval[0], new_interval[1]]
                else:
                    new_interval = [new_interval[0], intervals[idx][1]]
            else:
                res.append(new_interval)
                new_interval = intervals[idx]
        if new_interval:
            res.append(new_interval)
        return res