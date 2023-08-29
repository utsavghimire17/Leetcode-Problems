class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
            elif char in seen:
                count += 1
                seen = set()
                seen.add(char)
        if seen:
            count += 1
        return count