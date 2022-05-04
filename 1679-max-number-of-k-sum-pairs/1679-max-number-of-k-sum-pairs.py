class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        pairs = 0
        seen = set()
        
        for v1, cnt in counts.items():
            v2 = k - v1
            if v2 in seen: continue

            if v1 == v2:
                pairs += (cnt // 2)
            else:
                pairs += min(counts[v1], counts[v2])
            seen.add(v1)
                
        return pairs
            
            