
from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-i for i in nums]
        heapify(arr)
        while k:
            k -= 1
            num = heappop(arr)
            
        return -num