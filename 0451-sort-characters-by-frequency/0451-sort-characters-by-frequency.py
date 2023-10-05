class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        result = ""
        res = []
        for i in s:
            counter[i] = 1 + counter.get(i,0)
        for keys,values in counter.items():
            res.append([keys,values])
        res.sort(key = lambda x:x[1], reverse = True)
        print(res)
        for val in res:
            result += val[0] * val[1]
        return result
            