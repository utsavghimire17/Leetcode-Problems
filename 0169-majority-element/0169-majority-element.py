class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}
        n = len(nums)
        for i in nums:
            temp[i] = 1 + temp.get(i,0)
        for val in temp:
            if temp[val] > n//2 :
                return val