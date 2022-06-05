class MyQueue:

    def __init__(self):
        self.stk1 = deque()
        self.stk2 = deque()

    def push(self, x: int) -> None:
        self.stk1.append(x)        

    def pop(self) -> int:
        while len(self.stk1) > 1:
            self.stk2.append(self.stk1.pop())
        temp = self.stk1.pop()
        self.stk2.reverse()
        self.stk1, self.stk2 = self.stk2, self.stk1
        return temp

    def peek(self) -> int:
        return self.stk1[0]

    def empty(self) -> bool:
        return len(self.stk1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()