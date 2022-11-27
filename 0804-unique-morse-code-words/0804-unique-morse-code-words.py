class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        symbol_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--"   ,"-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        new_str = ""
        temp = set()
        for i in words:
            for char in i:
                new_str += symbol_list[ord(char) - ord("a")]
            temp.add(new_str)
            new_str = ""
        return len(temp)