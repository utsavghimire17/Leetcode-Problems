class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        start = 0
        end = len(needle) - 1
        index = -1
        n = 0
        while end < len(haystack) and n < len(needle):
            if haystack[start] == needle[n]:
                index = start
                for char in range(start, end + 1):
                    if n == len(needle):
                        break
                    if haystack[char] == needle[n]:
                        n += 1
                    else:
                        start += 1
                        end += 1
                        n = 0
                        break
            elif haystack[start] != needle[n]:
                index = -1
                n = 0
                start += 1
                end += 1
        if n == len(needle):
            return index
        return -1