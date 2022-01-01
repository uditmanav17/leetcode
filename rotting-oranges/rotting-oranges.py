class Solution:
    def get_unvisited_neighbours(self, row, col, grid, visited):
        neighbours = []

        # up
        if row > 0 and not visited[row-1][col] and grid[row-1][col] != 0:
            neighbours.append((row-1, col))

        # down
        if row < len(grid)-1 and not visited[row+1][col] and grid[row+1][col] != 0:
            neighbours.append((row+1, col))

        # left
        if col > 0 and not visited[row][col-1] and grid[row][col-1] != 0:
            neighbours.append((row, col-1))

        # right
        if col < len(grid[0])-1 and not visited[row][col+1] and grid[row][col+1] != 0:
            neighbours.append((row, col+1))

        for r, c in neighbours:
            visited[r][c] = True

        return neighbours

    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_time = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        # get all rotten oranges
        rotten_oranges = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_oranges.append((r, c, 0))
                    visited[r][c] = True
                    
        q = deque(rotten_oranges)
        
        # make remaining healthy oranges rotten
        while q:
            # print(q)
            r, c, time_ = q.popleft()
            max_time = max(max_time, time_)
            neighbours = self.get_unvisited_neighbours(r, c, grid, visited)
            q.extend([(x, y, time_ + 1) for x, y in neighbours])
            
        # check if any healthy orange remain
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    return -1
                
        return max_time
            
                    
        
                
        