class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start from top right
        r, c = 0, len(matrix[0]) - 1
        
        while c >= 0 and r < len(matrix):
            num = matrix[r][c]
            
            if num > target:
                c -= 1
            elif num < target:
                r += 1
            else:
                return True
            
        return False
        
        