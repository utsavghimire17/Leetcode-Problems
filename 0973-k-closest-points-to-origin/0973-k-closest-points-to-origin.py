class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for point in points:
            distance = (((point[1]) ** 2) + (point[0]) ** 2) ** 1/2
            distances.append([distance,point])
        distances.sort(key = lambda x:x[0])
        while len(distances) > k:
            distances.pop()
        for val in distances:
            res.append(val[1])
        return res