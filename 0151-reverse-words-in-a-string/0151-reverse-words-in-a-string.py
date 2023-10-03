class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        res = ""
        curr_string = ""
        space_count = 0
        for i in range(len(s)):
            if s[i] != " ":
                curr_string += s[i]
                space_count = 0
            else:
                space_count += 1
                if space_count == 1:
                    res = " " + curr_string + res
                curr_string = ""
                
        if curr_string:
            res = curr_string + res
        res.strip()
        return res