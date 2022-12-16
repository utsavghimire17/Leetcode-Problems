class MyQueue:

    def __init__(self):
        self.queue = []
        self.front = []

    def push(self, x: int) -> None:
        self.queue.append(x)
    def pop(self) -> int:
        if self.front == []:
            self.stack()
        return self.front.pop()
    def peek(self) -> int:
        if self.front == []:
            self.stack()
        return self.front[-1]

    def empty(self) -> bool:
        if self.front:
            return len(self.front) == 0
        return len(self.queue) == 0
    
    def stack(self):
        while self.queue:
            self.front.append(self.queue.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()