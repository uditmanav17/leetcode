class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Initilize two pointers
        begin = 0
        end = len(nums) - 1 
        
        while begin <= end:
            mid = (begin + end)//2
            if nums[mid] == target:
                return True
        
            # Fail to estimate which side is sorted
            if nums[mid] == nums[end]: 
                end -= 1  # In worst case: O(n)
            
            # Left side of mid is sorted
            elif nums[mid] > nums[end]: 
                # Target in the left side
                if  nums[begin] <= target and target < nums[mid]: 
                    end = mid - 1
                else: # in right side
                    begin = mid + 1
            
            # Right side is sorted
            else: 
                # Target in the right side
                if  nums[mid] < target and target <= nums[end]: 
                    begin = mid + 1
                else: # in left side
                    end = mid - 1
                    
        return False