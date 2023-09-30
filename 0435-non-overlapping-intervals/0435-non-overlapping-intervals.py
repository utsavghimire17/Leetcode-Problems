class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #basically if you take element with greater end range then it will have room to fit more intervals but if you take element with less end range then it can fit less intervals resulting in less overlapping
        intervals.sort(key = lambda x:x[1])
        
        curr_interval = intervals[0]
        count = 0
        print(intervals)
        for i in range(1,len(intervals)):
            if curr_interval[1] > intervals[i][0]:
                count += 1
            else:
                curr_interval = intervals[i]
        return count