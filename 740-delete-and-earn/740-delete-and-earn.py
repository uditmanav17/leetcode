from collections import Counter

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        ans = [0] * len(nums)
        # if one house, rob it
        ans[0] = nums[0]
        # if 2 houses, rob one with higher money
        ans[1] = max(nums[:2])
        
        # iterate over remaining
        for idx in range(2, len(nums)):
            # select max among - prev max, curr house money + prev prev max
            ans[idx] = max(ans[idx - 1], nums[idx] + ans[idx - 2])
            
        # print(ans)
        return ans[-1]
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        # we can reduce this to house robber problem - 198
        # arr will store element*count(element) in sorted order
        # sorting is required to simulate removing of elements
        # this arr will be used to solve house robber problem
        counts = Counter(nums)
        arr = [0] * (max(counts) + 1)
        
        for idx in range(len(arr)):
            arr[idx] = idx * counts.get(idx, 0)
            
        # check this arr for clarity
        # print(arr)
        return self.rob(arr)
        
        