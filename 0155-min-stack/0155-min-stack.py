from collections import deque
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append([val,min(val,self.stack[-1][1])])
        else:
            self.stack.append([val,val])
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        top = self.stack.pop()
        self.stack.append(top)
        return top[0]
    
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()