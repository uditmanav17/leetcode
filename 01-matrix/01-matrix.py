# https://leetcode.com/problems/01-matrix/discuss/1369881/Python-multi-source-bfs-explained

from itertools import product

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows, cols, visited, queue = len(mat), len(mat[0]), set(), deque()
        
        for r, c in product(range(rows), range(cols)):
            if mat[r][c] == 0:
                visited.add((r, c))
                queue.append((r, c))
        
        level = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dx, dy in dirs:
                    new_r = r + dx
                    new_c = c + dy
                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                        mat[new_r][new_c] = level
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
            # print(level, mat, queue)
                        
        return mat
        