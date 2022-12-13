class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
#         temp = {}
#         start = 0 
#         end = 0
#         matches = 0
#         for i in s1:
#             temp[i] = 1 + temp.get(i,0)
#         while end < len(s2):
#             if s2[end] in temp:

#                 temp[s2[end]] -= 1
#                 if temp[s2[end]] == 0:
#                     matches += 1
#             if end - start + 1 >= len(s1):
#                 if start > 0 and s2[start - 1] in temp:
#                     if temp[s2[start - 1]] == 0:
#                         matches -= 1
#                     temp[s2[start - 1]] += 1

#                 start += 1
#             if matches == len(temp):
#                 return True
#             end += 1
#         return False
        temp1 = {}
        temp2 = {}
        start = 0
        for i in s1:
            temp1[i] = 1 + temp1.get(i,0)
        for alp in "abcdefghijklmnopqrstuvwxyz":
            if alp not in temp1:
                temp1[alp] = 0
            temp2[alp] = 0
        for j in range(len(s2)):
            temp2[s2[j]] = 1 + temp2.get(s2[j],0)
            if j - start + 1 == len(s1):
                if temp2 == temp1:
                    return True
                temp2[s2[start]] -= 1
                start += 1
        return False
        