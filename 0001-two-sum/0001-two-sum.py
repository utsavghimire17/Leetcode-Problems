class Solution(object):
    def twoSum(self, nums, target):
        hold={}
        for i in range(len(nums)):
            if target-nums[i] in hold:
                return [hold[target-nums[i]],i]
            else:
                hold[nums[i]]=i
                        
        