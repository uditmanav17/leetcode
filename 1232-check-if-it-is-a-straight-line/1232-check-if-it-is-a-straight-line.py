
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x1, y1 = coordinates.pop()
        x2, y2 = coordinates.pop()
        
        rise = y2 - y1
        run = x2 - x1
        
        while coordinates:
            x, y = coordinates.pop()
            if (x-x1) * rise != (y-y1) * run:
                return False
        return True
