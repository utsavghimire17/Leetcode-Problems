class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = {}
        map_t = {}
        for c1,c2 in zip(s,t):
            if (c1 in map_s and map_s[c1] != c2) or (c2 in map_t and map_t[c2] != c1):
                return False
            map_s[c1] = c2
            map_t[c2] = c1
        return True