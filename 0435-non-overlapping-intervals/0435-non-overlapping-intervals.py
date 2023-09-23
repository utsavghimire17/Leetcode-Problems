class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        count = 0
        intervals.sort(key=lambda x:x[1])
        curr_interval = intervals[0]
        print(intervals)
        for idx in range(1,len(intervals)):
            if intervals[idx][0] < curr_interval[1]:
                count += 1
            else:
                curr_interval= intervals[idx]
        return count