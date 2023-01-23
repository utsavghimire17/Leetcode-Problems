class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cand = {}
        ignore = set()
        judge = -1
        if not trust:
            if n % 2 == 0:
                return -1
            return 1
        for i in trust:
            cand[i[1]] = []
            ignore.add(i[0])
        for i in trust:
            cand[i[1]].append(i[0])
        for cands in cand:
            if len(cand[cands]) == n - 1:
                if cands not in ignore:
                    return cands
        return -1
                
        