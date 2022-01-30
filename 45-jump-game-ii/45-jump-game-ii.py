class Solution:
    def jump(self, nums: List[int]) -> int:
        position = len(nums) - 1
        steps_taken = 0
        
        # till we have not reached first index
        while position != 0:
            # iterate over nums arr
            for idx in range(position):
                # if we can reach from curr_idx to last position
                # update position and continue while loop
                if nums[idx] >= position - idx:
                    position = idx
                    steps_taken += 1
                    break
        
        return steps_taken
        
        