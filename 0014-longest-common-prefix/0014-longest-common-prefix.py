class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for idx in range(len(strs[0])):
            current = strs[0][idx]
            for strings in strs:
                if idx == len(strings):
                    return common
                if strings[idx] != current:
                    return common
            common += current
        return common