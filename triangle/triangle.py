class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = [0] * (len(triangle) + 1)
        
        for row in reversed(triangle):
            for idx, num in enumerate(row):
                ans[idx] = num + min(ans[idx], ans[idx+1])
            # print(ans)
            
        return ans[0]
                
                    
        