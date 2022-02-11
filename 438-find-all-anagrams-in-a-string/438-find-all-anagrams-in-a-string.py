from collections import Counter
from string import ascii_lowercase

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counts = Counter({char:0 for char in ascii_lowercase})
        p_counts.update(p)
        
        s_counts = Counter({char:0 for char in ascii_lowercase})
        s_counts.update(s[:len(p)])
        
        ans = []
        if p_counts == s_counts:
                ans.append(0)
        
        # take one char at a time from 's'
        # and compare it with char counts of 'p'
        # if counts match, add first idx of sub string
        for idx in range(len(p), len(s)):
            remove_char = s[idx - len(p)]
            add_char = s[idx]
            # print(add_char, remove_char)
            
            s_counts[add_char] = s_counts[add_char] + 1
            s_counts[remove_char] = s_counts[remove_char] - 1
            
            if p_counts == s_counts:
                ans.append(idx - len(p) + 1)
                
        return ans
