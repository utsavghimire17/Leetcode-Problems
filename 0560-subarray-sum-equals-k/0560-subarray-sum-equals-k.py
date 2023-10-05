class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        # start=0
        # end=0
        # count=0
        # current_sum=0
        # while start<len(nums):
        #     current_sum+=nums[start]
        #     if nums[start]==k:
        #         count+=1
        #     while end<start and current_sum>=k:
        #         if current_sum==k:
        #             count+=1
        #             break
        #         else:
        #             current_sum-=nums[end]
        #             end+=1
        #     start+=1
        # return count
       
    # In this approach we calculate a pre sum and keep in the dictionary to record the count of the pre_sum occurenct. We also check another condition which is if pre_sum-k already exists in the dictionary becuase we know that if pre_sum - k already exists in the dictionary then within that sub array there is another sub array which gives us the required sum, k. If it exists then we increase the count and continue our iteration computing the pre_sum and it's count , if the pre_sum already exixts then we increase the count in the dictionary of that already pre-existent pre_sum. At last we return count. Also we need to initialize dictionary with pre_sum 0 and count of 1 because there may exist a case where only pre_computing the sum while iterating  may give us the required value k which would have a pre_sum value of 0. So, as we need to return 1 in this case we start with this base case i.e. {0:1}.
        
        presum_map = {0:1}
        pre_sum = 0
        res = 0
        for i in nums:
            pre_sum += i
            if pre_sum - k in presum_map:
                res += presum_map[pre_sum - k]
            if pre_sum in presum_map:
                presum_map[pre_sum] += 1
            else:
                presum_map[pre_sum] = 1
        return res
    