class Solution:
    def is_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (left + 1, right)
        
    def longestPalindrome(self, s: str) -> str:
        longest_palin = (0, 0)
        
        for idx in range(len(s)):
            odd_len_palin = self.is_palindrome(s, idx, idx)
            even_len_palin = self.is_palindrome(s, idx, idx+1)
            # print(odd_len_palin, even_len_palin)
            longest_palin = max(longest_palin, odd_len_palin, even_len_palin, 
                                key = lambda x : x[1] - x[0])
            
        return s[longest_palin[0]: longest_palin[1]]
        