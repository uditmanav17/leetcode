class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palin(mid1, mid2):
            while mid1 >= 0 and mid2 < len(s) and s[mid1] == s[mid2]:
                mid1 -= 1
                mid2 += 1
            return [mid1 + 1, mid2]
        
        
        longest = [0, 0]
        for idx in range(len(s)):
            odd_len_palin = is_palin(idx, idx)
            eve_len_palin = is_palin(idx, idx + 1)
            longest = max(longest, odd_len_palin, eve_len_palin, 
                          key=lambda x: x[1] - x[0])
            # print(idx, odd_len_palin, eve_len_palin, longest)
            
        return s[longest[0]:longest[1]]