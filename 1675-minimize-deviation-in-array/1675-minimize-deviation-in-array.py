# check notes

from heapq import heappush, heappop

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        
        min_val = float("inf")
        for num in nums:
            if num % 2 == 1:
                num *= 2
            min_val = min(min_val, num)
            heappush(heap, -num)
            
        diff = float("inf")
        while heap and heap[0] % 2 == 0:
            max_num = -1 * heappop(heap)
            diff = min(diff, max_num - min_val)
            min_val = min(min_val, max_num//2)
            heappush(heap, -max_num//2)
            
        # print(heap, diff, min_val)
        return min(diff, -1 * heappop(heap) - min_val)
        
        