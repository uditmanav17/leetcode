class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = Counter(nums)
        ans = 0
        if k == 0:
            ans = sum(1 for k, v in nums.items() if v >= 2)
            return ans 
        
        for n1 in nums:
            n2 = k + n1
            # print(n1, n2)
            if n2 in nums:
                ans += 1
            
        return ans
            