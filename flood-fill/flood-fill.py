

class Solution:
    def adjacent_cells(self, r, c, visited, image, color):
        max_r = len(image)
        max_c = len(image[0])
        adj_cells = []
        
        if 0 < r < max_r and not visited[r-1][c] and image[r-1][c] == color:
            adj_cells.append((r-1, c))
        if 0 <= r < max_r-1 and not visited[r+1][c] and image[r+1][c] == color:
            adj_cells.append((r+1, c))
            
        if 0 < c < max_c and not visited[r][c-1] and image[r][c-1] == color:
            adj_cells.append((r, c-1))
        if 0 <= c < max_c-1 and not visited[r][c+1] and image[r][c+1] == color:
            adj_cells.append((r, c+1))
            
        return adj_cells
        
    
    def floodFill(self, image: List[List[int]], 
                  sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = [[False] * len(image[0]) for _ in range(len(image))]
        queue = [(sr, sc)]
        visited[sr][sc] = True
        color = image[sr][sc]
        
        while queue:
            r, c = queue.pop(0)
            image[r][c] = newColor
            visited[r][c] = True
            queue.extend(self.adjacent_cells(r, c, visited, image, color))
        
        return image
        
        
        
        
        
        