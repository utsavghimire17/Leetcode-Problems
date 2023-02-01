import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = math.gcd(len(str1),len(str2))
        temp = n
        start1 = 0
        start2 = 0
        possible = str1[:n]
        while start1 < len(str1) or start2 < len(str2):
            if start2 < len(str2):
                if str2[start2 : n] != possible:
                   return ""
                start2 += temp
            if start1 < len(str1):
                if str1[start1:n] != possible:
                    return ""
                start1 += temp
            n += temp
        return possible

