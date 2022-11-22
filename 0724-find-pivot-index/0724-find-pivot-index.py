class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_arr = []
        postfix_arr = []
        curr_sum = 0
        total = sum(nums)
        for i in range(len(nums)):
            prefix_arr.append(curr_sum)
            postfix_arr.append(total-nums[i])
            curr_sum += nums[i]
            total -= nums[i]
        for idx in range(len(prefix_arr)):
            if prefix_arr[idx] == postfix_arr[idx] and prefix_arr != 0:
                return idx
        return -1