class Solution:
    def houseRob1(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        if n < 2:
            return nums[0]
        
        costs = [0] * n
        costs[0] = nums[0]
        costs[1] = max(nums[0], nums[1])
        
        for idx in range(2, n):
            costs[idx] = max(costs[idx - 1], costs[idx - 2] + nums[idx])
            
        return costs[-1]
        
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        a1, a2 = self.houseRob1(nums[1:]), self.houseRob1(nums[:-1])
        # print(a1, a2)
        return max(a1, a2)
        