class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_chars, m_chars = Counter(ransomNote), Counter(magazine)
        
        for r_char, cnt in r_chars.items():
            if cnt > m_chars.get(r_char, 0):
                return False
                
        return True

