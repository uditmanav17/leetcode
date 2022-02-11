class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        i, j = 0, cols - 1
        
        while 0 <= i < rows and 0 <= j < cols:
            num = matrix[i][j]
            # print(i, j, num)
            if num == target:
                return True
            elif num > target:
                j -= 1
            elif num < target:
                i += 1
            
        return False
        