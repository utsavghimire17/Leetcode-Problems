class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        result = ""
        res = []
        heapq.heapify(res)
        for i in s:
            counter[i] = 1 + counter.get(i,0)
        for keys,values in counter.items():
            heapq.heappush(res,(-1 * values,keys))
        while res:
            val = heapq.heappop(res)
            result += (-1*val[0]) * val[1]
        return result
            