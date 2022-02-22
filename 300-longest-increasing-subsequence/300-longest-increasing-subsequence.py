class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [1 for _ in range(len(nums))]
        
        for idx1 in range(len(nums)):
            n1 = nums[idx1]
            for idx2 in range(idx1):
                n2 = nums[idx2]
                if n2 < n1:
                    ans[idx1] = max(ans[idx1], ans[idx2] + 1)
                    
        # print(ans)
        return max(ans)
