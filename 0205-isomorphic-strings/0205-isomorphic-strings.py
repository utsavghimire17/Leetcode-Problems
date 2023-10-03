class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#         Created a counter map to keep track of number of elements and char_map to map the character of s to character of t.
        if len(s) != len(t):
            return False
        char_s = {}
        char_t = {}
        for i in range(len(s)):
            if s[i] in char_s and char_s[s[i]] not in char_t or t[i] in char_t and char_t[t[i]] not in char_s:
                return False
            if s[i] in char_s:
                if char_s[s[i]] != t[i]:
                    return False
            if t[i] in char_t:
                if char_t[t[i]] != s[i]:
                    return False
            if s[i] not in char_s and t[i] not in char_t:
                char_s[s[i]] = t[i]
                char_t[t[i]] = s[i]
        return True