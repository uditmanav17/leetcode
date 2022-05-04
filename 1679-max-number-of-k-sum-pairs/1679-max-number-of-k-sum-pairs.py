class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        pairs = 0
        
        for v1 in nums:
            cnt = counts.get(v1, 0)
            v2 = k - v1
        
            if v1 == v2:
                pairs += (cnt // 2)
            else:
                pairs += min(counts[v1], counts[v2])
                
            # so we don't count pair corresponding to (v2, v1)
            # after counting (v1, v2)
            counts[v2] = 0
            
                
        return pairs

