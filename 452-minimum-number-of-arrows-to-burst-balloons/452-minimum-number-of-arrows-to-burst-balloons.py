
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # something like merge intervals
        points.sort()
        ans = deque([points[0]])
        
        for idx in range(1, len(points)):
            curr_start, curr_end = points[idx]
            prev_start, prev_end = ans[-1]
            
            if prev_end >= curr_start:
                ans.pop()
                ans.append([max(curr_start, prev_start), min(curr_end, prev_end)])
            else:
                ans.append([curr_start, curr_end])
                
        # print(ans)
        return len(ans)
