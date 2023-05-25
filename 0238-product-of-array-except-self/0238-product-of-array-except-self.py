class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp, rp = [], []
        n = len(nums)
        
        for idx in range(n):
            n_l = nums[idx]
            if not lp:
                lp.append(n_l)
            else:
                lp.append(lp[-1] * n_l)
                
            n_r = nums[n - idx - 1]
            if not rp:
                rp.append(n_r)
            else:
                rp.append(rp[-1] * n_r)
                
        rp.reverse()
        lp.insert(0, 1)
        rp.append(1)
        
        # print(lp, rp)
        ans = []
        for idx in range(n):
            ans.append(lp[idx] * rp[idx + 1])
            
        return ans
            
        