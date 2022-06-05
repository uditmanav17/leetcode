class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
            else:
                return mid
        return -1
                
        