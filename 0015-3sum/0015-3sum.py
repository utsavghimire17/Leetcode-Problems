class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr_sum = 0
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue
            start = idx + 1
            end = len(nums) - 1
            while start < end:
                if start - 1 != idx and nums[start-1] == nums[start]:
                    start += 1
                    continue
                curr_sum = nums[idx] + nums[start] + nums[end]
                if curr_sum < 0:
                    start += 1
                elif curr_sum > 0:
                    end -= 1
                elif curr_sum == 0:
                    res.append([nums[idx],nums[start],nums[end]])
                    start += 1
        return res
    