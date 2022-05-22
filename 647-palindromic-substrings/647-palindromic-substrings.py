class Solution:
    def __init__(self):
        self.ans = 0
        
    def is_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.ans += 1
            left -= 1
            right += 1
        return (left + 1, right)
        
            
    def countSubstrings(self, s: str) -> int:
        for idx in range(len(s)):
            odd_len_palin = self.is_palindrome(s, idx, idx)
            even_len_palin = self.is_palindrome(s, idx, idx+1)
        
        return self.ans

        
        
        