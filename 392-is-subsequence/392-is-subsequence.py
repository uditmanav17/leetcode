class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        
        while i < len(s) and j < len(t):
            char_1 = s[i]
            char_2 = t[j]
            
            if char_1 == char_2:
                i += 1
                j += 1
            else: 
                j+= 1
            
        return i == len(s)
    