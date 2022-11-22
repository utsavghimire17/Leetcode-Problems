class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_arr = []
        postfix_arr = []
        curr_sum = 0
        total = sum(nums)
        count = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            prefix_arr.append(curr_sum)
            postfix_arr.append(total-nums[i])
            
            total -= nums[i]
            
        for idx in range(len(prefix_arr)-1):
            if prefix_arr[idx] >= postfix_arr[idx]:
                count += 1
        return count     