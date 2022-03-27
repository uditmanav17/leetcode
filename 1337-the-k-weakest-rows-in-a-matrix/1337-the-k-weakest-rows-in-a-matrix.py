class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        for idx, row in enumerate(mat):
            heappush(heap, (sum(row), idx))
            
        ans = []
        
        while k:
            _, idx = heappop(heap)
            ans.append(idx)
            k -= 1
            
        return ans
        