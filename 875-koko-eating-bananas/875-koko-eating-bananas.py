class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        beg, end = 0, max(piles)
        
        while beg + 1 < end:
            
            mid = beg + (end - beg) // 2
            
            bites = sum(ceil(i/mid) for i in piles)
            if bites > h:
                beg = mid
            else:
                end = mid
                
        return end
        