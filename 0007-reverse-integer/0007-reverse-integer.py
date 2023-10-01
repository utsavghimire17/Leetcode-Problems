class Solution(object):
    def reverse(self, x):
        negative = False
        
        if x < 0:
            x *= -1
            negative = True
        new_num = 0
        while x != 0:
            new_num = (new_num) * 10 + x % 10
            x //= 10
        if new_num >= 2**31 or new_num <= -2**31:
            return 0
        if negative:
            new_num *= -1
        return new_num            