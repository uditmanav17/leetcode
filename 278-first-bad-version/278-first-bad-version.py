# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        
        while l <= r:
            mid = l + (r - l) // 2
            
            curr_bad = isBadVersion(mid)
            prev_bad = isBadVersion(mid - 1)
            next_bad = isBadVersion(mid + 1)
            
            # print(l, mid, r)
            if curr_bad and not prev_bad:
                return mid
            elif curr_bad and prev_bad:
                r = mid - 1
            else:
                l = mid + 1
                
