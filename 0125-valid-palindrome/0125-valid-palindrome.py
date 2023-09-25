class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if ord(i.lower()) in range(97,123):
                new_str += i.lower()
            elif ord(i) in range(48,58):
                new_str += i
        start = 0
        end = len(new_str) - 1
        while start < end:
            if new_str[start] != new_str[end]:
                return False
            start += 1
            end -= 1
        return True