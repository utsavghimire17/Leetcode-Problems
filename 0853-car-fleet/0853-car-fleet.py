class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}
        stack = []
        for pos in range(len(position)):
            time[position[pos]] = (target - position[pos]) / speed[pos]
        print(time)
        position.sort()
        for pos in position:
            while stack and time[stack[-1]] <= time[pos]:
                stack.pop()
            stack.append(pos)
        return len(stack)