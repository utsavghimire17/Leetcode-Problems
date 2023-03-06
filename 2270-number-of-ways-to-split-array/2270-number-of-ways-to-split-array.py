class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = []
        postfix = []
        total = sum(nums)
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            prefix.append(curr_sum)
            postfix.append(total - num)
            total -= num
        for idx in range(len(nums) - 1):
            if prefix[idx] >= postfix[idx]:
                count += 1
        return count
            