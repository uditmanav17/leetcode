class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        N = len(nums)
        basket, rem = divmod(sum(nums), 4)
        if rem or nums[0] > basket: return False
        
        @cache
        def dfs(mask):
            if mask == 0: return 0
            for j in range(N):
                if mask & 1<<j:
                    neib = dfs(mask ^ 1<<j)
                    if neib >= 0 and neib + nums[j] <= basket:
                        return (neib + nums[j]) % basket
            return -1
                    
        return dfs((1<<N) - 1) == 0
