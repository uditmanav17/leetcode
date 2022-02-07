
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counts = Counter(s)
        t_counts = Counter(t)
        
        for char in t_counts:
            if t_counts[char] != s_counts.get(char, 0):
                return char
        