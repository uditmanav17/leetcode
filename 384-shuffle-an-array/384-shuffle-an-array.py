class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.backup = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.backup[:]
        return self.nums        

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for idx in range(n):
            swap_idx = randint(idx, n - 1)
            self.nums[idx], self.nums[swap_idx] = self.nums[swap_idx], self.nums[idx]
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()