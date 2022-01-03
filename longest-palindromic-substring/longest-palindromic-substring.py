class Solution:
    def is_palindrome(self, string, start, end):
        # expand outwards from indexes - start and end
        while start >= 0 and end < len(string) and string[start] == string[end]:
            start -= 1
            end += 1
        return [start + 1, end]
            
    
    def longestPalindrome(self, s: str) -> str:
        longest = [0, 1]
        
        for idx in range(len(s)):
            odd_palin = self.is_palindrome(s, idx, idx)
            even_palin = self.is_palindrome(s, idx, idx + 1)
            # print(odd_palin, even_palin)
            # print(s[odd_palin[0]: odd_palin[1]], s[even_palin[0]: even_palin[1]])
            longest = max([odd_palin, even_palin, longest], key=lambda x: x[1] - x[0])
            # print(idx, longest, s[longest[0]: longest[1]])
            
        return s[longest[0]: longest[1]]
            
        