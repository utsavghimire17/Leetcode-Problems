class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakpoint = -1
        i = 1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                breakpoint = i - 1
                break
        print(breakpoint)
        if breakpoint < 0:
            return nums.reverse()
        
        else:
            print(nums)
            print("T")
            next_max = float('inf')
            for j in range(breakpoint+1,len(nums)):
                if nums[j] > nums[breakpoint] and nums[j] <= next_max:
                    next_max = nums[j]
                    index = j
                
            print(next_max)
            
            nums[breakpoint],nums[index] = nums[index], nums[breakpoint]
            print(nums)
        start = breakpoint + 1
        end = len(nums) - 1
        while start <= end:
            if nums[start] > nums[end]:
                nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
        
        return nums
        
            