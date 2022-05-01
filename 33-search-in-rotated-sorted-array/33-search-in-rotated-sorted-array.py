class Solution:
    def binSearch(self, arr, l, r, target):
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] == target:
                return m
            elif arr[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
                
        
    
    def search(self, arr: List[int], target: int) -> int:
        # ans = self.binSearch([1,2,3,4,5,6,7,8,9], 0, 4, 5)
        # print(ans)

        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid] == target:
                return mid
            
            # left part of mid is sorted
            if arr[l] <= arr[mid]:
                if arr[l] <= target < arr[mid]:
                    return self.binSearch(arr, l, mid - 1, target)
                else:
                    l = mid + 1
            
            # right part of mid is sorted
            elif arr[mid] <= arr[r]:
                if arr[mid] < target <= arr[r]:
                    return self.binSearch(arr, mid + 1, r, target)
                else:
                    r = mid - 1
                    
        return -1
                
                
    
                
                