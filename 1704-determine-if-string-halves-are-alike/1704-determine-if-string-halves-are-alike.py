class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        count1 = 0
        count2 = 0
        for char in s[:len(s)//2]:
            if char in vowels:
                count1 += 1
        for char in s[len(s)//2:]:
            if char in vowels:
                count2 += 1
        return count1 == count2
                