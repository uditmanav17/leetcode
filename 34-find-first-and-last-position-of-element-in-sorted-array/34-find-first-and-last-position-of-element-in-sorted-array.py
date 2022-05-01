class Solution:
    def binInsert(self, arr, k):
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if arr[mid] < k:
                l = mid + 1
            else:
                r = mid - 1
                
        return l
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binInsert(nums, target)
        right = self.binInsert(nums, target + 1) - 1
        # print(left, right)
        
        return [left, right] if left <= right else [-1, -1]

        