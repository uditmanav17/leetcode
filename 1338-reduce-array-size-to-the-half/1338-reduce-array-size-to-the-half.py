
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        atleast_half = math.ceil(len(arr) / 2)
        heap = []
        
        for num, cnt in counts.items():
            heappush(heap, (-cnt, num))
            
        ans = count = 0
        while heap and count < atleast_half:
            ans += 1
            cnt, num = heappop(heap)
            count += abs(cnt)
            
        return ans
        
        
        
        
        
        