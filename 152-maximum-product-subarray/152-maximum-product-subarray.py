class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_prod, suff_prod = [], []
        
        n = len(nums)
        left_prod = right_prod = 1
        for idx in range(n):
            left_prod = left_prod or 1
            left_prod = (left_prod * nums[idx])
            pre_prod.append(left_prod)
            
            right_prod = right_prod or 1
            right_prod = (right_prod * nums[n - 1 - idx])
            suff_prod.append(right_prod)
            
        suff_prod = suff_prod[::-1]
        
        # print(pre_prod, suff_prod)
        ans = [max(i, j) for i, j in zip(pre_prod, suff_prod)]
        # print(ans)
        
        return max(ans)
        