class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum_arr = nums.copy()
        min_sum_arr = nums.copy()
        max_sum = nums[0]
        min_sum = nums[0]
        for i in range(1,len(nums)):
            max_sum_arr[i] = max(max_sum_arr[i], max_sum_arr[i] + max_sum_arr[i-1])
            max_sum = max(max_sum,max_sum_arr[i])
        for i in range(1,len(nums)):
            min_sum_arr[i] = min(min_sum_arr[i], min_sum_arr[i] + min_sum_arr[i-1])
            min_sum = min(min_sum, min_sum_arr[i])
            
        return max(abs(max_sum),abs(min_sum))