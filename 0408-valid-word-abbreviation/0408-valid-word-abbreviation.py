class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        end = 0
        count = 0
        temp = {'1':1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
        if word == abbr:
            return True
        while i < len(abbr) and end < len(word):
            if abbr[i] != word[end]:
                if abbr[i] in temp:
                    count = count * 10 + temp[abbr[i]]
                    if count == 0:
                        return False
                else:
                    if count:
                        end += count
                        count = 0
                        continue
                    else:
                        return False
            else:
                if count:
                    end += count
                    count = 0
                    continue
                else:
                    end += 1
            i += 1
        if count:
            end += count
        if end == len(word) and i == len(abbr):
            return True
        return False