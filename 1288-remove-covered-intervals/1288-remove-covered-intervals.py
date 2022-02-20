class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # custom sort - first on start point, next on (end-start)
        intervals.sort(key=lambda x: (x[0], -(x[1] - x[0])))
        # print(intervals)
        ans = [intervals[0]]
        
        for idx in range(1, len(intervals)):
            prev_start, prev_end = ans[-1]
            curr_start, curr_end = intervals[idx]
            
            if curr_start >= prev_start and curr_end <= prev_end:
                continue
            
            ans.append(intervals[idx])
            
        return len(ans)
        
        
            
                
        
        
        
        