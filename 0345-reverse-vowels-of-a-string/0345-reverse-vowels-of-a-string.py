class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_set = {"a","A","e","E","i","I","o","O","u","U"}
        vowels = [i for i in s]
        start = 0
        end = len(vowels) - 1
        while start < end:
            if vowels[start] in vowels_set and vowels[end] in vowels_set:
                vowels[start],vowels[end] = vowels[end],vowels[start]
                start += 1
                end -= 1
            elif vowels[start] in vowels_set and vowels[end] not in vowels_set:
                end -= 1
            elif vowels[end] in vowels_set and vowels[start] not in vowels_set:
                start += 1
            else:
                start += 1
                end -= 1
        return "".join(vowels)