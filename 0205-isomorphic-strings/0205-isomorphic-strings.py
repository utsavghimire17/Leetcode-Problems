class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        replace_map = dict()
        
        for i in range(len(s)):
            
            if s[i] in replace_map:
                if replace_map[s[i]] != t[i]:
                    return False
            else:
                replace_map[s[i]] = t[i]
        
        replace_map = dict()
        
        for i in range(len(t)):
            
            if t[i] in replace_map:
                if replace_map[t[i]] != s[i]:
                    return False
            else:
                replace_map[t[i]] = s[i]
        
        
        return True