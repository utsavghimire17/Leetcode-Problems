class Solution:
    def mySqrt(self, x: int) -> int:
        min_val = 0
        max_val = x
        mid_val = 0
        while int(min_val) < int(max_val):
            mid_val = (min_val + max_val)/2
            if int(mid_val*mid_val) == x:
                return int(mid_val)
            elif mid_val* mid_val < x:
                min_val = mid_val
            elif mid_val * mid_val > x:
                max_val = mid_val
        return int(min_val)