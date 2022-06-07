
class Solution:
    def calc_dist(self, x1, y1, x2=0, y2=0):
        return (abs(x1 - x2)**2 + abs(y2 - y1)**2)**0.5
    
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            heappush(heap, (self.calc_dist(x, y), x, y))
            
        ans = []
        while k:
            k -= 1
            _, x, y = heappop(heap)
            ans.append((x, y))
            
        return ans
        