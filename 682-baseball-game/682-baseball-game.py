class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = deque()
        
        for char in ops:
            if char not in "CD+":
                stack.append(int(char))
                continue
            if char == "C":
                stack.pop()
            if char == "D":
                stack.append(stack[-1] * 2)
            if char == "+":
                stack.append(stack[-1] + stack[-2])
                
        return sum(stack)

        