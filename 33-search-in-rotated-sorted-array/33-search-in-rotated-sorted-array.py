class Solution:
    def searchHelper(self, arr, l, r, target):
        
        while l <= r:
            mid = l + ((r - l) // 2)
            
            potential_match = arr[mid]
            left_num = arr[l]
            right_num = arr[r]
            
            if potential_match == target:
                return mid
            
            # left side is sorted
            elif left_num <= potential_match:
                if left_num <= target < potential_match:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # right side is sorted
            else:
                if potential_match < target <= right_num:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1
            
        
    
    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(nums, 0, len(nums) - 1, target)