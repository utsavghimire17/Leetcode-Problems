class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start = 0
        end = 0
        temp = {}
        count = len(t)
        min_window = float('inf')
        min_string = ""
        for char in t:
            temp[char] = 1 + temp.get(char,0)
        while end < len(s):
            while end < len(s) and count > 0:
                if s[end] in temp:
                    if temp[s[end]] > 0:
                        count -= 1
                    temp[s[end]] -= 1
                end += 1
            while start < end and count == 0:
                if min_window > end - start:
                    min_window = end - start
                    min_string = s[start:end]
                if s[start] in temp:
                    if temp[s[start]] >= 0:
                        count += 1
                    temp[s[start]] += 1
                
                start += 1
        return "".join(min_string)