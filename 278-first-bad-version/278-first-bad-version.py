# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        
        while l < r:
            mid = l + (r - l) // 2
            
            curr_bad = isBadVersion(mid)
            if curr_bad:
                r = mid 
            else:
                l = mid + 1
        return l
