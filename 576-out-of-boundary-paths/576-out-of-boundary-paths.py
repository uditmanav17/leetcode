class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 10**9+7
        
        @cache
        def dfs(N, i, j):
            if i == m or j == n or i < 0 or j < 0: return 1
            if N == 0: return 0
            
            return sum(
                dfs(N-1,i+x,j+y) 
                for x,y in [[-1,0],[1,0],[0,-1],[0,1]]
            ) % M
        
        return dfs(maxMove,startRow,startColumn)
    