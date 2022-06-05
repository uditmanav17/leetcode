class MinStack:

    def __init__(self):
        self.stk = deque()
        self.min_stk = deque()        

    def push(self, val: int) -> None:
        if not self.stk:
            self.min_stk.append(val)
        else:
            self.min_stk.append(min(val, self.min_stk[-1]))
        self.stk.append(val)

    def pop(self) -> None:
        self.min_stk.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()