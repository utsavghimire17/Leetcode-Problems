class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_diff = float('inf')
        max_val = 0
        
        for num in nums:
            curr_diff = abs(num - 0)
            
            if closest_diff > curr_diff:
                closest_diff = curr_diff
                closest_num = num
            elif closest_diff == curr_diff:
                if num > closest_num:
                    closest_num = num
        return closest_num