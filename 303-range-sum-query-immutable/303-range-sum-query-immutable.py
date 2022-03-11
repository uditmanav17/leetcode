class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = {}
        for idx, num in enumerate(nums):
            self.sums[idx] = self.sums.get(idx - 1, 0) + num
        # print(self.sums)
        
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)