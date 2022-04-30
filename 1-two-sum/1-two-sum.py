class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            t = target - num
            if t in seen:
                return [seen[t], idx]
            seen[num] = idx
        