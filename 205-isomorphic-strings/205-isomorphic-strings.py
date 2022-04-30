class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        
        for s_char, t_char in zip(s, t):
            s2t.setdefault(s_char, t_char)
            t2s.setdefault(t_char, s_char)
            # print(s2t, t2s)
            # print(s2t.get(t_char), t2s.get(s_char))
            if s2t.get(s_char) != t_char or t2s.get(t_char) != s_char:
                return False
            
        return True
        