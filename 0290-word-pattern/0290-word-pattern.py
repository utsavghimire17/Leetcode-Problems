class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        temp_p = {}
        temp_s = {}
        s_list = s.split(" ")
        if len(pattern) != len(s_list):
            return False
        for idx in range(len(pattern)):
            if (pattern[idx] in temp_p and temp_p[pattern[idx]] != s_list[idx]) or (s_list[idx] in temp_s and temp_s[s_list[idx]] != pattern[idx]):
                return False
            temp_p[pattern[idx]] = s_list[idx]
            temp_s[s_list[idx]] = pattern[idx]
            
        return True