class Solution:
    def uniquePathsWithObstacles(self, mat: List[List[int]]) -> int:
        if mat[0][0] == 1:
            return 0
        
        rows, cols = len(mat), len(mat[0])
        ans = [[0] * cols for _ in range(rows)]
        ans[0][0] = 1
        # print(ans)
        
        for r, c in product(range(rows), range(cols)):
            if mat[r][c] == 1 or (r == 0 and c == 0):
                continue
            if r == 0 and c > 0:
                ans[r][c] = ans[r][c-1]
            elif r > 1 and c == 0:
                ans[r][c] = ans[r-1][c]
            else:
                ans[r][c] = ans[r-1][c] + ans[r][c-1]
        
        # print(ans)
        
        return ans[-1][-1]
            
        