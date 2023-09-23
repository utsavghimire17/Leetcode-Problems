class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for idx in range(len(intervals)):
            if newInterval[1] < intervals[idx][0]:
                res.append(newInterval)
                return res + intervals[idx:]
            if newInterval[0] > intervals[idx][1]:
                res.append(intervals[idx])
            if newInterval[0] <= intervals[idx][1]:
                newInterval = [min(intervals[idx][0],newInterval[0]), max(intervals[idx][1],newInterval[1])]
        res.append(newInterval)
        return res
                