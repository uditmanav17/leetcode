class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # after k shifts, final array = grid
        k = k % (m * n)
        if k == 0:
            return grid

        div = gcd(m * n, k)  # math.gcd

        for i in range(div):
            r, c = divmod(i, n)
            curr = grid[r][c]

            for j in range(m * n // div):
                # get the resultant index
                r, c = divmod((i + k * (j + 1)) % (m * n), n)
                
                # perform swap operation
                grid[r][c], curr = curr, grid[r][c]  

        return grid

