class Solution:
    def __init__(self):
        self.romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,}
        
    def romanToInt(self, s: str) -> int:
        stack = deque()
        
        for char in s:
            num = self.romans[char]
            if not stack:
                stack.append(num)
                continue
            elif stack and stack[-1] < num:
                curr_num = stack.pop()
                stack.append(num - curr_num)
            else:
                stack.append(num)
            # print(char, num, stack)
            
        return sum(stack)
            
        