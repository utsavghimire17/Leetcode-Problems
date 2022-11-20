class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        temp_set = set(sentence)
            
        return len(temp_set) == 26
            
        