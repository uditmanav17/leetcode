
from itertools import product

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows, zeroCols = set(), set()
        rows, cols = len(matrix), len(matrix[0])
        
        # get all rows and cols having 0 element
        for r, c in product(range(rows), range(cols)):
            if matrix[r][c] == 0:
                zeroRows.add(r)
                zeroCols.add(c)
                
        # iterate over matrix and set elements as 0 
        for r, c in product(range(rows), range(cols)):
            if r in zeroRows or c in zeroCols:
                matrix[r][c] = 0
        