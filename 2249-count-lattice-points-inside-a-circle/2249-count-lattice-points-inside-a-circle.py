class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
        def euclid_dist(x1, y1, x2, y2):
            return sqrt((x2-x1)**2 + (y2-y1)**2)
        
        points = set()
        
        # remove duplicates
        circles = map(tuple, circles)
        circles = set(circles)
        
        for center_x, center_y, radius in circles:
            for x, y in product(range(center_x - radius, center_x + radius + 1), 
                                range(center_y - radius, center_y + radius + 1)):
                if euclid_dist(x, y, center_x, center_y) <= radius:
                    points.add((x, y))
                    
        return len(points)
