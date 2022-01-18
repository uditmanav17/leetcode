# add 0 at start and end of arr
# sliding window with group of 3 zeros

class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        
        arr = [0] + arr + [0]
        
        for idx in range(1, len(arr) - 1):
            if arr[idx - 1] == arr[idx] == arr[idx + 1] == 0:
                n -= 1
                arr[idx] = 1
                
        return n <= 0
            