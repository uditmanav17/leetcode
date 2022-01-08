
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        top_k = counts.most_common(k)
        
        # print(top_k)
        
        return [key for key, val in top_k]