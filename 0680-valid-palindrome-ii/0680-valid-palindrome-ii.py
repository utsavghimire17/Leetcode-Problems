class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) -1 
        count = 0
        while start < end:
            if s[start] != s[end]:
                if s[start+1: end + 1] == s[end:start:-1]:
                    start += 1
                elif s[start:end] == s[end-1:start:-1] + s[start]:
                    end -= 1
                else:
                    return False
            else:
                start += 1
                end -= 1
        return True