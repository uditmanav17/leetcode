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
        
        
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                visited[r][c] = True
                curr_max_area = 0
                if grid[r][c] == 0:
                    continue
                    
                q = [(r, c)]
                while q:
                    r, c = q.pop(0)
                    curr_max_area += 1
                    q.extend(self.get_unvisited_neighbours(r, c, grid, visited))
                
                max_area = max(max_area, curr_max_area)
                
        return max_area
                    
                
                
        