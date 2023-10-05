class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        res = []
        n = len(nums)
        for i in nums:
            counter[i] = 1 + counter.get(i,0)
        for keys,values in counter.items():
            if values > n/3:
                res.append(keys)
        return res
            