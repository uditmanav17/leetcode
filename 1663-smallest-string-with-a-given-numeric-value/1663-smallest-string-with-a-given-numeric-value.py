class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = [1] * n
        idx = n - 1
        k -= n
        
        while k:
            if k < 25:
                ans[idx] += k
                break
            else:
                k -= 25
                ans[idx] += 25
            idx -= 1
        
        return "".join([chr(i + 96) for i in ans])
        
            
        