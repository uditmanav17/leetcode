class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        chars = {}
        max_len = 0
        
        while r < len(s):
            right_char = s[r]
            chars.setdefault(right_char, 0)
            chars[right_char] += 1
            if chars[right_char] == 1:
                max_len = max(max_len, len(chars))
                
            while chars[right_char] > 1:
                max_len = max(max_len, len(chars))
                left_char = s[l]
                chars[left_char] -= 1
                if chars[left_char] == 0:
                    chars.pop(left_char)
                l += 1
            r += 1
            
        return max_len
                
                
        
        