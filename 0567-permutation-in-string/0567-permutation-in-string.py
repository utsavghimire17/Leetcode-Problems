class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp_s1 = {}
        temp_s2 = {}
        start = 0
        for i in "abcdefghijklmnopqrstuvwxyz":
            temp_s1[i] = 0
            temp_s2[i] = 0
        for i in s1:
            temp_s1[i] = 1 + temp_s1.get(i,0)
        for i in range(len(s2)):
            temp_s2[s2[i]] = 1 + temp_s2.get(s2[i],0)
            if i - start + 1 == len(s1):
                print(temp_s2)
                if temp_s1 == temp_s2:
                    return True
                temp_s2[s2[start]] -= 1
                start += 1
        return False
        
        