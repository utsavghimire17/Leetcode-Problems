class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps_count = {0:0}
        for row in wall:
            total = 0
            for col in range(len(row)-1):
                total += row[col]
                gaps_count[total] = 1 + gaps_count.get(total,0)
                
        return len(wall) - max(gaps_count.values())