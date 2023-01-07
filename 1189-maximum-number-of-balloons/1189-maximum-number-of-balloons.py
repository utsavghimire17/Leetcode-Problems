class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        temp = {}
        min_val = float('inf')
        for char in text:
            if char in "balloon":
                temp[char] = 1 + temp.get(char,0)
        if len(temp) < 5:
            return 0
        for char in temp:
            if char == "a" or char == "b" or char == "n":
                if temp[char] < 1:
                    return 0
                min_val = min(min_val, temp[char])
            elif char == "l" or char == "o":
                if temp[char] < 2:
                    return 0
                min_val = min(min_val,(temp[char]//2))
        return min_val