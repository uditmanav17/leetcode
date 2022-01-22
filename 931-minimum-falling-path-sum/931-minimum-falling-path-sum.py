class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        ans = [0] * n
        
        for row in matrix:
            temp_ans = ans[:]
            for idx, num in enumerate(row):
                # print(idx, num, temp_ans)
                ans[idx] = num + min(temp_ans[idx - 1] if idx > 0 else float("inf"), 
                                     temp_ans[idx], 
                                     temp_ans[idx + 1] if idx < n-1 else float("inf")
                                    )
                # print(idx, ans)
        # print(ans)
        
        return min(ans)
    