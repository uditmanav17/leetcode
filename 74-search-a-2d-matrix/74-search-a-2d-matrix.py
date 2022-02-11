# https://leetcode.com/problems/search-a-2d-matrix/discuss/26248/6-12-lines-O(log(m)-%2B-log(n))-myself%2Blibrary

# treat the matrix like a single big list of length m*n and use a simple binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        l, r = 0, rows * cols - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            num = matrix[mid//cols][mid%cols]
            
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            elif num > target:
                r = mid - 1
                
        return False
        