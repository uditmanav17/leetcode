class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        
        for i, j in product(range(rows), range(cols)):
            live_neighbors = 0
            
            for r, c in directions:
                new_r, new_c = i + r, j + c
                if (0 <= new_r < rows
                    and 0 <= new_c < cols
                    and abs(board[new_r][new_c]) == 1
                   ): 
                    live_neighbors += 1
            
            # print(i, j, live_neighbors)
            
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                # will be marked dead
                board[i][j] = -1
            elif board[i][j] == 0 and live_neighbors == 3:
                # will come alive
                board[i][j] = 2
                
        # print(board)
        for i, j in product(range(rows), range(cols)):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1
            
            
                
        