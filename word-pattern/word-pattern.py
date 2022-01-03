class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = {}
        word_to_pattern = {}
        
        if len(pattern) != len(s.split()):
            return False
        
        for pattern, word in zip(pattern, s.split()):
            if pattern in pattern_to_word and pattern_to_word[pattern] != word:
                return False
            if word in word_to_pattern and word_to_pattern[word] != pattern:
                return False
            
            word_to_pattern[word] = pattern
            pattern_to_word[pattern] = word
            
        return True
        
        