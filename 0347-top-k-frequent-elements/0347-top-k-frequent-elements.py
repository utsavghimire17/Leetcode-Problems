class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}
        rslt = []
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        
        rslt = sorted(hash_map, key = lambda x: hash_map[x], reverse = True)
        return rslt[:k]