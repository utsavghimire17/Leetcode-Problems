class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for i in range(len(digits)-1,-1,-1):
            if carry:
                if digits[i] == 9:
                    res.append(0)
                else:
                    res.append(digits[i] + carry)
                    carry = 0
            else:
                res.append(digits[i])
        if carry:
            res.append(1)
        return res[::-1]