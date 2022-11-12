class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                count += 1
            if s[i] == " " and count:
                return count
        return count