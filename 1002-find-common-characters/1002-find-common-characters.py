class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        old_dict = {}
        new_dict = {}
        res = []
        new_str = ""
        for char in words[0]:
            if char not in old_dict:
                old_dict[char] = 1
            else:
                old_dict[char] += 1

        for idx in range(1,len(words)):
            for j in range(len(words[idx])):
                if words[idx][j] in old_dict and old_dict[words[idx][j]] > 0:
                    if words[idx][j] not in new_dict:
                        new_dict[words[idx][j]] = 1
                    else:
                        new_dict[words[idx][j]] += 1
                    old_dict[words[idx][j]] -= 1
            if idx == len(words) - 1:
                break
            old_dict = new_dict
            new_dict = {}
        for char in new_dict:
            new_str = (char*new_dict[char])
            res.extend(new_str)
        return res
            
                        