class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        temp_count = [0] * 26
        count = 0
        for i in chars:
            temp_count[ord(i) - ord("a")] += 1
        for word in words:
            word_count = [0] * 26
            for char in word:
                word_count[ord(char) - ord("a")] += 1
            for i in range(len(word_count)):
                if word_count[i] > temp_count[i]:
                    break
            else:
                count += len(word)
        return count
            