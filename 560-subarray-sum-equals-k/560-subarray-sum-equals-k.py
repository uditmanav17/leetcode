# soln approach 3

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        counts = {0:1}
        total = ans = 0
        
        for idx in range(len(nums)):
            # calculate jump in cumsum
            total += nums[idx]
            
            # check difference bw current sum and target 
            diff = total - k
            ans += counts.get(diff, 0)
            
            counts[total] = counts.get(total, 0) + 1
            
        return ans
