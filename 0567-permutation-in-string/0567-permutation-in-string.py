class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        temp = {}
        start = 0
        matched = 0
        for char in s1:
            if char not in temp:
                temp[char] = 1
            elif char in temp:
                temp[char] += 1
        for i in range(len(s2)):
            if s2[i] in temp:
                temp[s2[i]] -= 1
                if temp[s2[i]] == 0:
                    matched += 1
            if i >= len(s1) and s2[i - len(s1)] in temp:
                if temp[s2[i-len(s1)]] == 0:
                    matched -= 1
                temp[s2[i-len(s1)]] += 1
                
                     
            if matched == len(temp):
                     return True
        return False