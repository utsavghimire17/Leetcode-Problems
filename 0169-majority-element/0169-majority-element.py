class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        end = 0
        start = 0
        max_val = 0
        nums.sort()
        while end < len(nums):
            if nums[start] == nums[end]:
                max_val = max(max_val,end-start+1)
                if max_val > len(nums)//2:
                    return nums[start]
                end += 1
            elif nums[start] != nums[end]:
                start = end