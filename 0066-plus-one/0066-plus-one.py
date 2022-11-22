class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = False
        res = [1]
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            elif digits[i] != 9:
                digits[i] = digits[i] + 1
                val = True
                break
            elif digits[i] == 0:
                digits[i] = digits[i] + 1
                val = True
                break
        if val == False:
            res.extend(digits)
            return res
        return digits