
class Solution:
    def maxProduct(self, nums: "list[int]") -> int:
        prefix, suffix, max_so_far = 0, 0, nums[0]
        n = len(nums)
        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[n - i - 1]
            max_so_far = max(max_so_far, prefix, suffix)

            # print(f"{i=}\t{~i=}\t{nums[~i]=}")
            # print(prefix, suffix, max_so_far)

        return max_so_far
        
        