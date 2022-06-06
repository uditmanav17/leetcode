
class Solution:
    def final_string(self, s: str):
        stack = deque()
        
        for char in s:
            if stack and char == "#":
                stack.pop()
            elif char != "#":
                stack.append(char)
        
        return "".join(stack)
    
    
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        # print(self.final_string(s), self.final_string(t))
        return self.final_string(s) == self.final_string(t)
        
        