class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for strings in strs:
            char = [0] * 26
            for ch in strings:
                char[ord(ch) - ord('a')] += 1
            if tuple(char) in anagrams:
                anagrams[tuple(char)].append(strings)
            else:
                anagrams[tuple(char)] = [strings]
        return list(anagrams.values())