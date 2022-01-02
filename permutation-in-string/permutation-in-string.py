
from collections import Counter
from string import ascii_lowercase

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter({char:0 for char in ascii_lowercase})
        s1_counts.update(s1)
        
        s2_counts = Counter({char:0 for char in ascii_lowercase})
        s2_counts.update(s2[:len(s1)])
        
        # sliding window
        for idx in range(len(s2) - len(s1)):
            if s1_counts == s2_counts:
                return True
            
            # delete prev char
            s2_counts[s2[idx]] -= 1
            
            # add new char
            s2_counts[s2[idx + len(s1)]] += 1
            
            # print(idx)
            # print(s1_counts)
            # print(s2_counts)
        
        return s1_counts == s2_counts
            
            
        
        