class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def can_split(upperBoundSubarraySum, subNums, m):
            curr_subarr_sum = 0
            cnt_subarr = 1
            
            for n in subNums:
                curr_subarr_sum += n
                if curr_subarr_sum > upperBoundSubarraySum:
                    cnt_subarr += 1
                    curr_subarr_sum = n
                    if cnt_subarr > m:
                        return False
                    
            return True
        
        
        min_val = float("-inf")
        max_val = 0
        
        for num in nums:
            min_val = max(min_val, num)
            max_val += num
            
        while min_val < max_val:
            mid = min_val + (max_val - min_val) // 2
            if can_split(mid, nums, m):
                max_val = mid
            else:
                min_val = mid + 1
                
        return min_val
            
        