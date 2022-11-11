class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp=set()
        maxlength=0
        start=0

        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[start])
                start+=1
            temp.add(s[i])
            maxlength=max(maxlength,i-start+1)
        return maxlength