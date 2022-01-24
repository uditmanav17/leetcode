
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppers = 1 if word[0].isupper() else 0
        for idx in range(1, len(word)):
            prev_char = word[idx-1]
            curr_char = word[idx]
            
            uppers += 1 if curr_char.isupper() else 0
            if prev_char.islower() and curr_char.isupper():
                return False
            
        if 1 < uppers < len(word):
            return False 
        
        return True
