# https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
# https://leetcode.com/problems/burst-balloons/discuss/76241/Another-way-to-think-of-this-problem-(Matrix-chain-multiplication)



class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def MatrixChainOrder(p, n): 
            m = [[0 for x in range(n)] for x in range(n)] 
            for i in range(1, n): 
                m[i][i] = 0

            # L is chain length. 
            for L in range(2, n): 
                for i in range(1, n-L + 1): 
                    j = i + L-1
                    m[i][j] = float("-inf") 
                    for k in range(i, j): 
                        q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j] 
                        if q > m[i][j]: 
                            m[i][j] = q 

            return m[1][n-1]

        nums=[1]+nums+[1]
        return MatrixChainOrder(nums, len(nums))