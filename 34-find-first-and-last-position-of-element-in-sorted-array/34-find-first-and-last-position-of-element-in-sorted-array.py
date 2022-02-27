class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(arr, k):
            l, r = 0, len(arr) - 1
            
            while l <= r:
                m = l + ((r - l) >> 2)
                # print(l, m, r)
                
                if nums[m] < k:
                    l = m + 1
                else:
                    r = m - 1
                    
            return l
        
        left = search(nums, target)
        # print(left)
        right = search(nums, target + 1) - 1
        
        # print(left, right)
        return [-1, -1] if left > right else [left, right]
                    
        