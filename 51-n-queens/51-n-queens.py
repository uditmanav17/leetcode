class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def mark_board(board, i, j):
            for x, y in product(range(n), range(n)):
                # mark current queen position 
                # and all squares it can capture as "."
                if x == i or y == j or abs(x - i) == abs(y - j):
                    board[x][y] = "."
            board[i][j] = "Q"
            
            
        # place queen on i-th row
        def recur(board, row):
            for col in range(n):
                if board[row][col] == "0":
                    unmarked_board = copy.deepcopy(board)
                    mark_board(board, row, col)
                    # Found a valid solution
                    if sum(curr_row.count('Q') for curr_row in board) == n:
                        res.append(copy.deepcopy(board))
                        return
                    # next row
                    else:
                        recur(board, row + 1)
                    board = unmarked_board
                    
        res = []            
        board = [["0"] * n for _ in range(n)]
        recur(board, 0)
        return [[''.join(row) for row in board] for board in res]
                    
        