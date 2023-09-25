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
        curr_sum = temp[s[-1]]
        curr = temp[s[-1]]
        for idx in range(len(s)-2,-1,-1):
            if temp[s[idx]] < curr:
                curr_sum -= temp[s[idx]]
            else:
                curr_sum += temp[s[idx]]
            curr = temp[s[idx]]
        return curr_sum