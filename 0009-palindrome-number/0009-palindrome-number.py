class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = x
        temp = 0
        if x == 0:
            return True
        if x % 10 == 0 or x < 0:
            return False
        while temp < val:
            temp = temp * 10 + (x % 10)
            x = x // 10
        return val == temp