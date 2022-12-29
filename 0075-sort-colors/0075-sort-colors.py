class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_colors = [0] * 3
        prev_index = 0
        for num in nums:
            sorted_colors[num] += 1
        for idx in range(len(sorted_colors)):
            nums[prev_index:prev_index + sorted_colors[idx] + 1] = [idx] * sorted_colors[idx]
            prev_index += sorted_colors[idx]
        return nums   