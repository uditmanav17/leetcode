# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/discuss/820072/EASY-soultion-with-DRY-RUN-JAVA

# dry run
# elements      :   9    5    8    2    -6    4    -3    0    2    -5    15    10    -7    9    -2
# positive_len  :   1    2    3    4     0    1     7    0    1     0     1     2     5    6     5
# negative_len  :   0    0    0    0     5    6     2    0    0     2     3     4     3    4     7

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = neg = ans = 0
        
        for num in nums:
            if num > 0:
                pos, neg = 1 + pos, 1 + neg if neg else 0
            elif num < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos = neg = 0
            
            ans = max(pos, ans)
            
        return ans
        