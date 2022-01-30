class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxPos = i = 0

        # iterate over nums arr, till we can proceed
        while i <= maxPos:
            # at each index, check maximum possible reach
            # and assign it to maxPos
            maxPos = max(maxPos, i + nums[i])
            # if we have cross last index, return True
            if maxPos >= n - 1:
                return True
            i += 1

        return False

