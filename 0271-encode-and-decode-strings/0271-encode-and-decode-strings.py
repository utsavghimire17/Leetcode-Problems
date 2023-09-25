class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "*" + string
        print(encoded_string)
        return encoded_string
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(s): 
            length = ""
            while s[i] != "*":
                length += s[i]
                i += 1
            res.append(s[i+1:i+int(length)+1])
            i = i + int(length) + 1
        return res
                      

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))