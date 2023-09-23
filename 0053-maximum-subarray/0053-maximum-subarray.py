class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum,curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
        # max_sum = nums[0]
        # for i in range(1,len(nums)):
        #     nums[i] = max(nums[i], nums[i] + nums[i-1])
        #     max_sum = max(nums[i],max_sum)
        # return max_sum