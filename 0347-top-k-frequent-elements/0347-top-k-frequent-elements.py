class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        frequency = []
        res = []
        for num in nums:
            temp[num] = 1 + temp.get(num,0)
        for keys,values in temp.items():
            frequency.append((keys,values))
        frequency.sort(key=lambda x:x[1], reverse = True)
        for idx in range(k):
            res.append(frequency[idx][0])
        return res
            