class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_vol = 0
        while start < end:
            if height[end] >= height[start]:
                volume = height[start] * (end -  start)
                start += 1
            elif height[end] < height[start]:
                volume = height[end] * (end-start)
                end -= 1
            max_vol = max(max_vol, volume)
        return max_vol