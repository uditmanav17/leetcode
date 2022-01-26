class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        beg, end = 1, max(piles)
        
        while beg < end:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            mid = beg + (end - beg) // 2
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            bites = sum(ceil(pile/mid) for pile in piles)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if bites > h:
                beg = mid + 1
            else:
                end = mid
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.       
        return end
