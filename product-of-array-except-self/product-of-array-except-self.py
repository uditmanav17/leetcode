# https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = list(accumulate(nums, mul))
        suf = list(accumulate(nums[::-1], mul))[::-1]
        n = len(nums)
        return [(pre[i-1] if i else 1) * (suf[i+1] if i+1 < n else 1) for i in range(n)]
        