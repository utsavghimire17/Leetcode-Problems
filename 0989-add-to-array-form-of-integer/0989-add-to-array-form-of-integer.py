class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        digit = 0
        res = []
        for i in num:
            digit = digit * 10 + i
        digit += k
        while digit != 0:
            res.append(digit % 10)
            digit = digit // 10
        return res[::-1]