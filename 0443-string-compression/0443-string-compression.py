class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        start = 0
        end = 0
        count = 0
        res = []
        while end < len(chars):
            if chars[start] == chars[end]:
                end += 1
                count += 1
            else:
                if count >= 2:
                    for i in str(count):
                        start += 1
                        chars[start] = i
                count = 0
                start += 1
                chars[start] = chars[end]
                
        else:
            if count >= 2:
                for i in str(count):
                    start += 1
                    chars[start] = i
            count = 0
            start += 1
        return start
            