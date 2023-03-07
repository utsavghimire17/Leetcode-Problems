class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")
        for num in nums:
            if num >= first:
                third = second
                second = first
                first = num
            elif num < first and num >= second:
                third = second
                second = num
            elif num < second and num >= third:
                third = num
        
        first_min = float("inf")
        second_min = float("-inf")
        for num in nums:
            if num <= first_min:
                second_min = first_min
                first_min = num
            elif num > first_min and num <= second_min:
                second_min = num
        
        return max((first*second*third),(first_min*second_min*first))
            
    