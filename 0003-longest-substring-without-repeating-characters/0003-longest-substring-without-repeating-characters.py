class Solution(object):
    def lengthOfLongestSubstring(self, s):
        check = set()
        start = 0
        end = 0
        max_window = 0
        while end < len(s):
            while s[end] in check:
                check.remove(s[start])
                start += 1
            check.add(s[end])
            max_window = max(max_window, end - start + 1)
            end += 1
        return max_window