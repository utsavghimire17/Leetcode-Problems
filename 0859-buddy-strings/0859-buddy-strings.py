class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        temp_s  = {}
        temp_goal = {}
        diff = 0
        for i in range(len(s)):
            temp_s[s[i]] = 1 + temp_s.get(s[i],0)
            temp_goal[goal[i]] = 1 + temp_goal.get(goal[i],0)
        if temp_s != temp_goal:
            return False
        for idx in range(len(s)):
            if s[idx] != goal[idx]:
                diff += 1
        if diff == 0:
            for char in temp_s:
                if temp_s[char] > 1:
                    return True
            return False
        return diff == 2
        