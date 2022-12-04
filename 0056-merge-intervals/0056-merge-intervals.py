class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        new_intervals = sorted(intervals, key = lambda x:x[0])
        res = []
        temp = new_intervals[0]
        i = 0
        if len(new_intervals) == 1:
            return [temp]
        while i < len(new_intervals):
            if temp[1] in range(new_intervals[i][0],new_intervals[i][1]+1):
                temp = [temp[0],new_intervals[i][1]]
            elif new_intervals[i][1] in range(temp[0],temp[1]):
                temp = [temp[0],temp[1]]
            else:
                res.append(temp)
                temp = new_intervals[i]
            i += 1
        else:
            res.append(temp)
        return res