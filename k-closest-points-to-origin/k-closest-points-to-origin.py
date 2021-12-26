# from heapq import heappush, heappop

class Solution:
    def origin_dist(self, y1, y2):
        return ((0 - y1)**2 + (0 - y2)**2)**0.5
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        
        for x1, x2 in points:
            d = self.origin_dist(x1, x2)
            heappush(points_heap, (d, [x1, x2]))
        
        answer = []
        while len(answer) < k and points_heap:
            _, point = heappop(points_heap)
            answer.append(point)
            
        return answer
            
        