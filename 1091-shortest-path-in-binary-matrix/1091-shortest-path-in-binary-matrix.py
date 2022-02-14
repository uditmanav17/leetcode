class Solution:
    
    def get_unvisited_neighbours(self, row, col, grid, visited):
        neighbours = []

        # up
        if row > 0 and not visited[row - 1][col] and grid[row - 1][col] != 1:
            neighbours.append((row - 1, col))

        # down
        if row < len(grid) - 1 and not visited[row + 1][col] and grid[row + 1][col] != 1:
            neighbours.append((row + 1, col))

        # left
        if col > 0 and not visited[row][col - 1] and grid[row][col - 1] != 1:
            neighbours.append((row, col - 1))

        # right
        if col < len(grid[0]) - 1 and not visited[row][col + 1] and grid[row][col + 1] != 1:
            neighbours.append((row, col + 1))

        # upper-left
        if (
            row > 0
            and col > 0
            and not visited[row - 1][col - 1]
            and grid[row - 1][col - 1] != 1
        ):
            neighbours.append((row - 1, col - 1))

        # upper-right
        if (
            row > 0
            and col < len(grid[0]) - 1
            and not visited[row - 1][col + 1]
            and grid[row - 1][col + 1] != 1
        ):
            neighbours.append((row - 1, col + 1))

        # lower-left
        if (
            row < len(grid) - 1
            and col > 0
            and not visited[row + 1][col - 1]
            and grid[row + 1][col - 1] != 1
        ):
            neighbours.append((row + 1, col - 1))

        # lower-right
        if (
            row < len(grid) - 1
            and col < len(grid[0]) - 1
            and not visited[row + 1][col + 1]
            and grid[row + 1][col + 1] != 1
        ):
            neighbours.append((row + 1, col + 1))

        for r, c in neighbours:
            visited[r][c] = True

        return neighbours


    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        q = deque([(0, 0, 1)])
        ans = float("inf")
        
        while q:
            r, c, path_length = q.popleft()
            if r == (rows - 1) and c == (cols - 1):
                ans = min(path_length, ans)
                
            neighbours = self.get_unvisited_neighbours(r, c, grid, visited)
            q.extend((r, c, path_length + 1) for r, c in neighbours)
            
        return ans if ans != float("inf") else -1
                
            
        
        