class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + ((r - l) >> 1)
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # search on the right side, because smaller elements are in the right side
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # search the minimum in the left side
                r = mid - 1

