class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        temp = {"0","1","8","9","6"}
        six_count = 0
        nine_count = 0
        if num[0]!= "6" and num[0] != "9":
                if num[0] != num[len(num)-1]:
                    return False
        for i in range(len(num)):
            if num[i] not in temp:
                return False
            if num[i] == "6":
                six_count += 1
            elif num[i] == "9":
                nine_count += 1
        if six_count != nine_count:
            return False
        return True
            