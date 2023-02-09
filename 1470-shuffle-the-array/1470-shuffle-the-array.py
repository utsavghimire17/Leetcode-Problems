class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        rslt = []
        mid = n
        
        for i in range(n):
            rslt.append(nums[i])
            rslt.append(nums[mid])
            mid += 1
        
        return rslt
            
        