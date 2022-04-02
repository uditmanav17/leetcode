class Solution:
    def validPalindrome(self, inp_str: str) -> bool:
        
        def is_palindrome(s, i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
                
            return True
        
        
        left, right = 0, len(inp_str) - 1
        
        while left <= right:
            if inp_str[left] != inp_str[right]:
                return (is_palindrome(inp_str, left + 1, right) 
                        or is_palindrome(inp_str, left, right - 1))
            
            left += 1
            right -= 1
            
        return True
        
            
            
        