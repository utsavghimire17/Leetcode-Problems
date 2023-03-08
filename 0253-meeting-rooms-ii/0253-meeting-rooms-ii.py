class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [i[0] for i in intervals]
        start.sort()
        end = [i[1] for i in intervals]
        end.sort()
        
        s = 0
        e = 0
        res = 0
        count = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res