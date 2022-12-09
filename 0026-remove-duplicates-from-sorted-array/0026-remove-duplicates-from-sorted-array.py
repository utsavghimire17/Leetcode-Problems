class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 1
        repeated_val = None
        repeated = False
        while end < len(nums):
            if nums[start] != nums[end] and repeated_val == None :
                start += 1
                end += 1
            else:
                repeated = True
                if repeated_val == None:
                    start += 1
                    repeated_val = nums[start]
                if nums[end] != repeated_val:
                    nums[start] = nums[end]
                    repeated_val = nums[start]
                    start += 1
                    end += 1
                else:
                    end += 1
        if repeated == False:
            return len(nums)
        return start