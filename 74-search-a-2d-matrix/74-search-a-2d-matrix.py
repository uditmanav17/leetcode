class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            curr_r, curr_c = divmod(mid, cols)
            ele = matrix[curr_r][curr_c]
            # print(mid, curr_r, curr_c)
            # print(l, mid, r, ele)
            
            if ele == target:
                return True
            elif ele < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False
        