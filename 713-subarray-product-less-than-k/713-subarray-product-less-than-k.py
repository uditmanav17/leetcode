class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        product = 1
        left_ptr = ans = 0
        
        # expand window
        for right in range(len(nums)):
            product *= nums[right]
            
            # contract window till product < target
            while product >= k:
                product /= nums[left_ptr]
                left_ptr += 1
                
            # update answer - the number of intervals with subarray product less than k 
            # and with right-most coordinate right, is (right - left + 1)
            ans += (right - left_ptr + 1)
            
        return ans

