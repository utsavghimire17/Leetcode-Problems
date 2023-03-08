class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = {}
        for idx in range(len(order)):
            order_map[order[idx]] = idx
        for idx in range(len(words)-1):
            if words[idx] == words[idx+1]:
                continue
            for i in range(min(len(words[idx]),len(words[idx+1]))):
                if order_map[words[idx][i]] > order_map[words[idx+1][i]]:
                    return False
                elif order_map[words[idx][i]] < order_map[words[idx+1][i]]:
                    break
                if i == len(words[idx+1]) - 1:
                    return False
        return True
            