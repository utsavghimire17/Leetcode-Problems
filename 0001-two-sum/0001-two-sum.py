class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx in range(len(nums)):
            if target - nums[idx] in hash_map:
                return [idx, hash_map[target-nums[idx]]]
            hash_map[nums[idx]] = idx
        return -1