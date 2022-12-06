class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#         Created a counter map to keep track of number of elements and char_map to map the character of s to character of t.
        temp_s = {}
        temp_t = {}
        char_map = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            temp_s[s[i]] = 0 + temp_s.get(s[i],0)
            temp_t[t[i]] = 0 + temp_t.get(t[i],0)
        for idx in range(len(s)):
            temp_s[s[idx]] += 1
            temp_t[t[idx]] += 1
            if s[idx] not in char_map:
                char_map[s[idx]] = t[idx]
            if temp_s[s[idx]] != temp_t[t[idx]] or char_map[s[idx]] != t[idx]:
                   return False
        return True