from itertools import product


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # precompute sub matrix sum
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        dp_mat = [[0] * (cols) for _ in range(rows)]

        for r, c in product(range(1, rows), range(1, cols)):
            dp_mat[r][c] = (
                dp_mat[r - 1][c]  # prev_row
                + dp_mat[r][c - 1]  # prev_col
                - dp_mat[r - 1][c - 1]  # prev_row/prev_col
                + matrix[r - 1][c - 1]  # curr matrix element
            )
        self.dp_mat = dp_mat

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (
            self.dp_mat[r2 + 1][c2 + 1]
            - self.dp_mat[r1][c2 + 1]
            - self.dp_mat[r2 + 1][c1]
            + self.dp_mat[r1][c1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

