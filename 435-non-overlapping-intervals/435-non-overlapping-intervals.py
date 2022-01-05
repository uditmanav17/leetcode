# https://leetcode.com/problems/non-overlapping-intervals/discuss/1097728/Python-concise-greedy-solution

# First sort the intervals by the left edge, and iterate through the sorted intervals, 
# when we encouter a overlap, discard the one with larger right edge 
# because it has greater chance to overlap with others in the future.


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        remove = 0
        prev_end = float("-inf")
        
        for idx, (start, end_) in enumerate(intervals):
            # no overlap
            if start >= prev_end:
                # update prev_end to current interval end as no overlap
                prev_end = end_
            else:
                remove += 1
                
        return remove
                
            
        
        