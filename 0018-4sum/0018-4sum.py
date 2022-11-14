class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
                
        nums.sort()

        arb1 = 0
        arb2 = 1
        res = []
        while arb1 < len(nums) - 3:
            if arb1 > 0 and nums[arb1] == nums[arb1-1]:
                arb1 += 1
                continue
            arb2 = arb1 + 1
            while arb2 < len(nums) - 2:
                if arb2 - 1!= arb1 and nums[arb2]== nums[arb2-1]:
                    arb2 += 1
                    continue
                start = arb2 + 1
                end = len(nums) - 1
                while start < end:
                    if start - 1 != arb2 and nums[start] == nums[start-1]:
                        start += 1
                        continue
                    curr_sum = nums[arb1] + nums[arb2] + nums[start] + nums[end]
                    if curr_sum < target:
                        start += 1
                    elif curr_sum > target:
                        end -= 1
                    else:
                        res.append([nums[arb1],nums[arb2],nums[start],nums[end]])
                        start += 1
                arb2 += 1
            arb1 += 1
        return res