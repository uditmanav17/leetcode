class Solution:
    
    def get_unvisited_neighbours(self, row, col, grid, visited):
        neighbours = []

        # up
        if row > 0 and not visited[row-1][col] and grid[row-1][col] != 'X':
            neighbours.append((row-1, col))

        # down
        if row < len(grid)-1 and not visited[row+1][col] and grid[row+1][col] != 'X':
            neighbours.append((row+1, col))

        # left
        if col > 0 and not visited[row][col-1] and grid[row][col-1] != 'X':
            neighbours.append((row, col-1))

        # right
        if col < len(grid[0])-1 and not visited[row][col+1] and grid[row][col+1] != 'X':
            neighbours.append((row, col+1))

        for r, c in neighbours:
            visited[r][c] = True

        return neighbours

    
    def dfs(self, r, c, mat, visited):
        visited[r][c] = True
        q = deque([(r, c)])
        
        while q:
            r, c = q.popleft()
            neighbours = self.get_unvisited_neighbours(r, c, mat, visited)
            q.extend(neighbours)
        
          
    def solve(self, matrix: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        
        # traverse all corner blocks and run DFS
        # top row
        for col in range(cols):
            if matrix[0][col] == 'O':
                self.dfs(0, col, matrix, visited)
                
        # last row
        for col in range(cols):
            if matrix[rows-1][col] == 'O':
                self.dfs(rows-1, col, matrix, visited)
                
        # first col
        for row in range(rows):
            if matrix[row][0] == 'O':
                self.dfs(row, 0, matrix, visited)
                
        # last col
        for row in range(rows):
            if matrix[row][cols-1] == 'O':
                self.dfs(row, cols-1, matrix, visited)
                
        
        for r, c in product(range(rows), range(cols)):
            if matrix[r][c] == 'O' and not visited[r][c]:
                matrix[r][c] = 'X'
                
        