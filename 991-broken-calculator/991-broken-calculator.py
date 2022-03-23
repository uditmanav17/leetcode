class Solution:
    def brokenCalc(self, start: int, end: int) -> int:
        # return self.recur_brokenCalc(start, end)
        return self.iterative_brokenCalc(start, end)
    
    
    def iterative_brokenCalc(self, start: int, end: int) -> int:
        ans = 0
        
        while start < end:
            ans += 1
            
            if end % 2 == 0:
                end //= 2
            else:
                end += 1
                
        return ans + abs(end - start)
    
        
    def recur_brokenCalc(self, start: int, end: int) -> int:
        if start >= end:
            return start - end
        
        if end % 2 == 0:
            end //= 2
        else:
            end += 1
            
        return 1 + self.recur_brokenCalc(start, end)
            