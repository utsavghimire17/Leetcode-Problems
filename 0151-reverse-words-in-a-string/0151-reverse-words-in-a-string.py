class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = len(s)
        curr_word = ""
        count = 0
        for i in range(len(s) - 1 , -1 ,-1):
            if s[i] == " ":
                count += 1
                if count > 1:
                    j = i
                    continue
                curr_word += s[i+1:j] + " "
                j = i
            else:
                count = 0
        else:
            curr_word += s[i:j] 
        return curr_word.strip()