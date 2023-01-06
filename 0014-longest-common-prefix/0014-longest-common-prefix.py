class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for index in range(len(strs[0])):
            curr_char = strs[0][index]
            for char in strs:
                if index == len(char) or char[index] != curr_char:
                    return prefix
            prefix += curr_char
        return prefix
                    
            