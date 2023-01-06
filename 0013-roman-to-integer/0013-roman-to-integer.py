class Solution:
    def romanToInt(self, s: str) -> int:
        temp = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        int_sum = temp[s[-1]]
        for idx in range(len(s)-1):
            if temp[s[idx]] < temp[s[idx + 1]]:
                int_sum -= temp[s[idx]]
            else:
                int_sum += temp[s[idx]]
        return int_sum