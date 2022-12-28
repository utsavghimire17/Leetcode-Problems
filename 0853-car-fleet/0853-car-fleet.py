class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_track = {}
        for idx in range(len(position)):
            speed_track[position[idx]] = speed[idx]
        position.sort()
        stack = []
        for cars in position:
            while stack and speed_track[stack[-1]] > speed_track[cars]:
                if cars + (speed_track[cars] * ((cars - stack[-1])/(speed_track[stack[-1]] - speed_track[cars])) ) > target:
                    break
                stack.pop()
            stack.append(cars)
        return len(stack)