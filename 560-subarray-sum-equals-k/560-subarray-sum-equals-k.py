class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total = ans = 0
        counts = {0:1}
        
        for num in nums:
            # get cumsum
            total += num
            
            # get diff bw target and curr_cumsum
            diff = total - k
            
            # check if diff is already seen and add it to ans
            ans += counts.get(diff, 0)
            
            # add curr_cumsum to counts
            counts[total] = counts.get(total, 0) + 1
        
        return ans
            
            
        
        
        