from math import sqrt
from heapq import heappush, heappop

class Solution:
    def origin_dist(self, x, y):
        return sqrt(x**2 + y**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []
        
        for x, y in points:
            dist = self.origin_dist(x, y)
            heappush(heap, (dist, x, y))
            
        # print(heap)
        for _ in range(k):
            t, x, y = heappop(heap)
            ans.append((x, y))
            
        return ans
            