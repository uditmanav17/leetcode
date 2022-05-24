class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxValid = 0
        opening = closing = 0
        
        for char in s:
            if char == '(':
                opening += 1
            elif char == ')':
                closing += 1
            if closing > opening:
                closing = opening = 0
            
            if opening == closing:
                currMax = opening * 2
                maxValid = max(maxValid, currMax)
                
        
        opening = closing = 0
        for char in s[::-1]:
            if char == ')':
                opening += 1
            elif char == '(':
                closing += 1
            if closing > opening:
                closing = opening = 0
            
            if opening == closing:
                currMax = opening * 2
                maxValid = max(maxValid, currMax)
                
        return maxValid
        