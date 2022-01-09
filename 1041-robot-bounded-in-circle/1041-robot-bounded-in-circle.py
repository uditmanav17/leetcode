# https://leetcode.com/problems/robot-bounded-in-circle/discuss/850437/Python-O(n)-solution-explained

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        
        for char in 4*instructions:
            if char == "G": x, y = x + dx, y + dy
            if char == "L": dx, dy = -dy, dx
            if char == "R": dx, dy = dy, -dx
        
        return (x, y) == (0, 0)
