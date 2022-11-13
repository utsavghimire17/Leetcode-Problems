class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        val_set = set()
        result = []
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for key,val in temp.items():
            val_set.add((key,val))
            if len(val_set) > k:
                val_set.remove(min(val_set,key = lambda x:x[1]))
        for items in val_set:
            result.append(items[0])
        return result