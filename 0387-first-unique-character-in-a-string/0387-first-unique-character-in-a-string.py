class Solution:
    def firstUniqChar(self, s: str) -> int:
        banned_set = set()
        counter = {}
        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = i
            elif s[i] in counter:
                banned_set.add(s[i])
        for char in s:
            if char not in banned_set:
                return counter[char]
        return -1