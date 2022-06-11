
class Solution:
    def minOperations(self, arr: List[int], x: int) -> int:
        arr_sum = sum(arr)
        new_target = arr_sum - x
        # print(arr_sum, new_target)
        
        start_idx = curr_sum = 0
        max_len = -float("inf")
        
        for end_idx in range(len(arr)):
            curr_sum += arr[end_idx]
            
            while start_idx <= end_idx and curr_sum > new_target:
                curr_sum -= arr[start_idx]
                start_idx += 1
            
            if curr_sum == new_target:
                max_len = max(max_len, end_idx - start_idx + 1)
        
        ans = (len(arr) - max_len) if max_len != -float("inf") else -1 
        return ans
            
        
        
        
        