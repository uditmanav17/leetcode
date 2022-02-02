class Solution:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counts = Counter(p)
        s_counts = Counter(s[:len(p)])
        ans = []
        
        if p_counts == s_counts:
            ans.append(0)
            
        # take one char at a time from 's'
        # and compare it with char counts of 'p'
        # if counts match, add first idx of sub string
        for add_char_idx in range(len(p), len(s)):
            remove_char_idx = add_char_idx - len(p)
            add_char = s[add_char_idx]
            rem_char = s[remove_char_idx]
            # print(add_char_idx, remove_char_idx)
            
            s_counts[add_char] = s_counts.get(add_char, 0) + 1
            s_counts[rem_char] -= 1
            if s_counts[rem_char] == 0:
                s_counts.pop(rem_char)
            
            # print(p_counts, s_counts)
            if p_counts == s_counts:
                ans.append(remove_char_idx+1)
            
        return ans
            
            
            
            
            