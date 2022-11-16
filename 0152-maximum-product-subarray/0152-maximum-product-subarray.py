class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = 1 
        curr_max = 1
        ans = max(nums)
        for i in nums:
            temp = curr_max
            curr_max = max(i,curr_max*i,curr_min*i)
            curr_min = min(i,temp*i,curr_min*i)
            ans = max(ans,curr_max)
        return ans