class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            if tuple(sorted(string)) not in anagrams:
                anagrams[tuple(sorted(string))] = [string]
            elif tuple(sorted(string)) in anagrams:
                anagrams[tuple(sorted(string))].append(string)
        print(anagrams)
        return list(anagrams.values())