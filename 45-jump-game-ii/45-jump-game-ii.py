class Solution:
    def jump(self, nums: List[int]) -> int:
        maxRange = steps = nums[0]
        jumps = 0
        
        if steps == 0 or len(nums) == 1:
            return 0
        
        for idx in range(1, len(nums)-1):
            num = nums[idx]
            # check max reachable index
            maxRange = max(maxRange, num + idx)
            steps -= 1

            # if we don't have any steps to take, 
            # we jump
            if steps == 0:
                jumps += 1
                steps = maxRange - idx
            # print(f"{steps=}")

        return jumps + 1