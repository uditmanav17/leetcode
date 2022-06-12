
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counts = {}
        start_idx = max_sum = curr_sum = 0
        
        for end_idx in range(len(nums)):
            num = nums[end_idx]
            curr_sum += num
            
            counts.setdefault(num, 0)
            counts[num] += 1
            if counts[num] <= 1:
                max_sum = max(max_sum, curr_sum)
            
            while start_idx <= end_idx and counts[num] > 1:                
                left_num = nums[start_idx]
                curr_sum -= left_num
                counts[left_num] -= 1
                if counts[left_num] == 0:
                    counts.pop(left_num)
                start_idx += 1

            
        return max_sum
        