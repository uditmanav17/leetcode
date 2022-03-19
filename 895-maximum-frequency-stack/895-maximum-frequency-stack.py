class FreqStack:

    def __init__(self):
        self.counts = {}
        self.stacks = []
        

    def push(self, val: int) -> None:
        self.counts[val] = self.counts.get(val, 0) + 1
        
        if len(self.stacks) < self.counts[val]:
            self.stacks.append([val])
        else:
            stack_to_insert_in = self.counts[val]
            self.stacks[stack_to_insert_in - 1].append(val)
            
        # print(self.stacks, self.counts)
        

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        self.counts[val] -= 1
        
        if not self.stacks[-1]:
            self.stacks.pop()
            
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()