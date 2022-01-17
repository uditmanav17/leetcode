
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        
        pattern_to_words = {}
        words_to_pattern = {}
        
        for curr_pattern, word in zip(pattern, s.split()):
            if curr_pattern in pattern_to_words and pattern_to_words.get(curr_pattern) != word:
                return False
                
            if word in words_to_pattern and words_to_pattern.get(word) != curr_pattern:
                return False
            
            words_to_pattern[word] = curr_pattern
            pattern_to_words[curr_pattern] = word
            
        return True
    
    