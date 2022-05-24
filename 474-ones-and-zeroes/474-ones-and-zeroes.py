class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [(i.count("0"), i.count("1")) for i in strs]
        
        @cache
        def select_fn(start_idx, zeros, ones):
            if zeros < 0 or ones < 0:
                return float("-inf")
            
            if start_idx >= len(strs):
                return 0
            
            curr_z, curr_o = counts[start_idx]
            
            return max(
                select_fn(start_idx + 1, zeros - curr_z, ones - curr_o) + 1,
                select_fn(start_idx + 1, zeros, ones)
            )
        
        return select_fn(0, m, n)
        
        
        