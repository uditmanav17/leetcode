class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * wt for wt in stones]
        heapify(max_heap)
        
        while len(max_heap) >= 2:
            s1 = abs(heappop(max_heap))
            s2 = abs(heappop(max_heap))
            
            if s1 == s2:
                continue
                
            new_wt = abs(s1 - s2)
            heappush(max_heap, -new_wt)
            
        
        return -max_heap[0] if max_heap else 0
        
        
        
        