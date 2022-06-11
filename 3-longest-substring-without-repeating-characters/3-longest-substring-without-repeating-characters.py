class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_idx = 0
        chars = {}
        max_len = 0
        
        for end_idx in range(len(s)):
            right_char = s[end_idx]
            chars.setdefault(right_char, 0)
            chars[right_char] += 1
            if chars[right_char] == 1:
                max_len = max(max_len, len(chars))
                
            while chars[right_char] > 1:
                max_len = max(max_len, len(chars))
                left_char = s[start_idx]
                chars[left_char] -= 1
                if chars[left_char] == 0:
                    chars.pop(left_char)
                start_idx += 1
            
            
        return max_len
                
                
        
        