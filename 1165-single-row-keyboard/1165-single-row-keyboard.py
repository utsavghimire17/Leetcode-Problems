class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        result = 0
        index = 0
        counter = {}
        for i, char in enumerate(keyboard):
            counter[char] = i
        for char in word:
            result += abs(index - counter[char])
            index = counter[char]
        return result