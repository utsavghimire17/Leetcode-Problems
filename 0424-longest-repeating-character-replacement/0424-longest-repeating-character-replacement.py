class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0
        temp = {}
        max_i = -1
        max_w = 0
        while end < len(s):
            temp[s[end]] = 1 + temp.get(s[end],0)
            for i in temp:
                 if temp[i] > max_i:
                    max_i = temp[i]
            window = end - start + 1
            if window - max_i <= k:
                 max_w = max(max_w, end - start + 1)
            else:
                 temp[s[start]] -= 1
                 start += 1
            end += 1
        return max_w
