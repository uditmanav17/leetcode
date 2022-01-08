
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
                
            if char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(idx)

        for idx in stack:
            s[idx] = ""
            
        return "".join(s)
                
        