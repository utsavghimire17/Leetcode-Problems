class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = set()
        freq = {}
        res = []
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        for keys,values in freq.items():
            top_k.add((keys,values))
            if len(top_k) > k:
                top_k.remove(min(top_k, key=lambda x:x[1]))
        for val in top_k:
            res.append(val[0])
        return res