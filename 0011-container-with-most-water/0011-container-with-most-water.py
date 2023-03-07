class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) -1 
        max_volume = 0
        while start < end:
            if height[start] < height[end]:
                volume = height[start] * (end - start)
                start += 1
            elif height[end] <= height[start]:
                volume = height[end] * (end - start)
                end -= 1
            max_volume = max(max_volume, volume)
        return max_volume