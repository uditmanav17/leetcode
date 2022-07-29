class Solution:
    
    def matchPattern(self, word, pattern):
        m1, m2 = {}, {}
        
        for ch1, ch2 in zip(word, pattern):
            if ch1 not in m1:
                m1[ch1] = ch2
                
            if ch2 not in m2:
                m2[ch2] = ch1
                
            if (m1[ch1], m2[ch2]) != (ch2, ch1):
                return False
        return True
    
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return filter(lambda word: self.matchPattern(word, pattern), words)
    
    