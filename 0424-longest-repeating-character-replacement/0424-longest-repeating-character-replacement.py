class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = {}
        start = 0
        max_val = -1
        max_window = 0
        for i in range(len(s)):
            temp[s[i]] = 1 + temp.get(s[i],0)
            for val in temp:
                if temp[val] > max_val:
                    max_val = temp[val]
            window = i - start + 1
            if window - max_val <= k:
                max_window = max(max_window,window)
            else:
                temp[s[start]] -= 1
                start += 1
        return max_window