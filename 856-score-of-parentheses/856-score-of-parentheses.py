class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = deque([])
        
        for char in s:
            if char == "(":
                stack.append(char)
            
            else:
                # found '()'
                if stack and stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                    continue
                
                # while consecutive numbers
                curr_total = 0
                while stack and isinstance(stack[-1], int):
                    curr_total += stack.pop()
                    
                # depth of brackets
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(2 * curr_total)
                    
        # print(stack)
        
        return sum(stack)
