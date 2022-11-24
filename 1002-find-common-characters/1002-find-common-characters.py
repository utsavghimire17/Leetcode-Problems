class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        minimum_words = [float("inf")] * 26
        res = []
        for word in words:
            current_words = [0] * 26
            for char in word:
                current_words[ord(char) - ord("a")] += 1
                
            for i in range(len(current_words)):
                minimum_words[i] = min(minimum_words[i],current_words[i])
        
        for i in range(len(minimum_words)):
            if minimum_words[i] != 0:
                res.extend(chr(97+i)*minimum_words[i])
        return res 