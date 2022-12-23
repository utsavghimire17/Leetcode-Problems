class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        have = 0
        window = {}
        temp = {}
        res = [-1,-1]
        res_len = float('inf')
        for i in t:
            temp[i] = 1 + temp.get(i,0)
        need = len(temp)
        for r in range(len(s)):
            if s[r] in temp:
                window[s[r]] = 1 + window.get(s[r],0)
                if window[s[r]] == temp[s[r]]:
                    have += 1
            while have == need:
                if res_len > r - l + 1:
                    res_len = r - l + 1
                    res = [l,r]
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < temp[s[l]]:
                        have -= 1
                l += 1
        return s[res[0]:res[1]+1]        