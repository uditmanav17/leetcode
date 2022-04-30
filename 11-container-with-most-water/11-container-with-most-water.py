class Solution:
    def maxArea(self, arr: List[int]) -> int:
        maxWater = 0
        l_idx, r_idx = 0, len(arr) - 1
        
        
        while l_idx < r_idx:
            diff = abs(r_idx - l_idx)
            l_max, r_max = arr[l_idx], arr[r_idx]
            water_area = min(l_max, r_max) * diff
            maxWater = max(maxWater, water_area)
            
            if l_max < r_max:
                l_idx += 1
            else:
                r_idx -= 1
                
        return maxWater
        