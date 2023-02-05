class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for idx  in range(len(order)):
            order_map[order[idx]] = idx
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                continue
            for idx in range(min(len(words[i]),len(words[i+1]))):
                if order_map[words[i][idx]] > order_map[words[i+1][idx]]:
                    return False
                elif order_map[words[i][idx]] < order_map[words[i+1][idx]]:
                    break
                if idx == len(words[i+1]) - 1:
                    return False
        return True