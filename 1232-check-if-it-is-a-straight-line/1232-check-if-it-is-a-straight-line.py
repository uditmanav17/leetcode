
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        slopes = set()
        
        x0, y0 = coordinates[0]
        for idx in range(1, len(coordinates)):
            x1, y1 = coordinates[idx]
            
            numerator = y1 - y0
            deno = x1 - x0
            
            if deno == 0:
                slopes.add(float("inf"))
                continue 
            
            slope = numerator / deno
            slopes.add(slope)
            
        if len(slopes) > 1:
            return False
        
        return True
            
        