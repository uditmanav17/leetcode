class Solution:
    def hIndex(self, citations: List[int]) -> int:
        heap = []
        
        h_index = 0
        
        for ele in citations:
            heappush(heap, ele)
            
            while heap and heap[0] <= h_index:
                heappop(heap)
                
            if len(heap) >= h_index + 1:
                h_index += 1
                
            
                
        return h_index
            