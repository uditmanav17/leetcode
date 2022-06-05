class Solution:
    def get_neighbors(self, r, c, mat, visited, color_to_replace):
        neighbors = []
        deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        for dx, dy in deltas:
            nr, nc = r + dx, c + dy
            if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]) \
            and not visited[nr][nc] and mat[nr][nc] == color_to_replace:
                neighbors.append((nr, nc))
                
        return neighbors
        
    
    def floodFill(self, image: List[List[int]], 
                  sr: int, sc: int, 
                  newColor: int) -> List[List[int]]:
        
        visited = [[False] * len(image[0]) for _ in range(len(image))]
        q = deque([(sr, sc)])
        color_to_replace = image[sr][sc]
        
        while q:
            r, c = q.pop()
            image[r][c] = newColor
            visited[r][c] = True
            nbrs = self.get_neighbors(r, c, image, visited, color_to_replace)
            # print(nbrs)
            q.extend(nbrs)
            
        return image
        