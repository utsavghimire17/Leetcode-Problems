class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        temp = {}
        end = 0
        diff = 0
        for nums in bills:
            temp[nums] = 1 + temp.get(nums,0)
            if nums - 5 != 0:
                if nums - 5 == 5:
                    if nums - 5 in temp:
                        if temp[nums-5] >= (nums-5)//5:
                            temp[nums-5] -= (nums-5)//5
                            continue
                    return False
                elif nums - 5 > 5:
                    if 10 in temp and temp[10] >= 1:
                        if 5 in temp and temp[5] >= 1:
                            temp[10] -= 1
                            temp[5] -=1
                        else:
                            return False
                    elif 5 in temp:
                        if temp[5] >= (nums-5)//5:
                            temp[5] -= (nums-5)//5
                        else:
                            return False
                    else:
                        return False

        return True

