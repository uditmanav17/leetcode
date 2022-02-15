class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR everything
        ans = 0
        for ele in nums:
            ans ^= ele
        return ans