class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # arr of (max_lcs_length, occurance)
        ans = [[1, 1] for _ in range(len(nums))]
        
        for idx1 in range(len(nums)):
            n1 = nums[idx1]
            for idx2 in range(idx1):
                n2 = nums[idx2]
                
                if n2 < n1:
                    curr_long_at_idx1 = ans[idx1][0]
                    new_long_at_idx1 = ans[idx2][0] + 1
                    
                    # if both are equal, increase curr occurance count 
                    if new_long_at_idx1 == curr_long_at_idx1:
                        ans[idx1][1] += ans[idx2][1]
                    
                    # if new is longer, update length and occurance count
                    elif new_long_at_idx1 > curr_long_at_idx1:
                        ans[idx1][0] = new_long_at_idx1
                        ans[idx1][1] = ans[idx2][1]

        # print(ans)
        max_subseq_len, instances = max(ans)
        
        # count of sequences with max length
        return sum(j for i, j in ans if i == max_subseq_len)
