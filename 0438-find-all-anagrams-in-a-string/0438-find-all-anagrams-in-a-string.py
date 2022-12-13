class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        end = 0
        temp1 = {}
        temp2 = {}
        res = []
        for i in p:
            temp1[i] = 1 + temp1.get(i,0)
        for alph in "abcdefghijklmnopqrstuvwxyz":
            if alph not in temp1:
                temp1[alph] = 0
            temp2[alph] = 0
        while end < len(s):
            temp2[s[end]] += 1
            if end - start + 1 == len(p):
                if temp1 == temp2:
                    res.append(start)
                temp2[s[start]] -= 1
                start += 1
            end += 1
        return res