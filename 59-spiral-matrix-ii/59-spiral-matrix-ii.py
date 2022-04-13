class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        dx, dy = 1, 0
        x, y = 0, 0
        
        for idx in range(n * n):
            # assign to cell
            mat[y][x] = idx + 1
            
            # check if out of bounds or already assigned
            if not 0 <= x + dx < n or not 0 <= y + dy < n or mat[y+dy][x+dx] != 0:
                # change directions
                dx, dy = -dy, dx
                
            # update x and y
            x, y = x + dx, y + dy
            
        return mat
