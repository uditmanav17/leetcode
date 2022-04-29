class Solution:
    def isMonotonic(self, arr: List[int]) -> bool:
        monotonic_inc = monotonic_dec = True
        
        for idx in range(1, len(arr)):
            prev_ = arr[idx - 1]
            next_ = arr[idx]
            
            if prev_ > next_:
                monotonic_inc = False
                
            if prev_ < next_:
                monotonic_dec = False
                
        return monotonic_inc or monotonic_dec
