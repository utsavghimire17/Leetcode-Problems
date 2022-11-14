class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        curr_idx = 0
        curr_diff = 0
        min_diff = float('inf')
        while curr_idx < len(nums) - 2:
            start = curr_idx + 1
            end = len(nums) -  1
            while start < end:
                curr_sum = nums[curr_idx] + nums[start] + nums[end]
                curr_diff = abs(curr_sum - target)
                if min_diff > curr_diff:
                    min_diff = curr_diff
                    closest_sum = curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    start += 1
                else:
                    end -= 1
            curr_idx += 1
        return closest_sum 