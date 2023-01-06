class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            if target - nums[i] in temp:
                return [i,temp[target - nums[i]]]
            temp[nums[i]] = i