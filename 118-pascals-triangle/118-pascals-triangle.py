class Solution:
    def __init__(self):
        self.triangle = [[1], [1, 1]]
        
        while len(self.triangle) < 30:
            prev_row = self.triangle[-1]
            next_row = [a + b
                        for a, b in zip(prev_row + [0], [0] + prev_row)]
            self.triangle.append(next_row)
            
    def generate(self, numRows: int) -> List[List[int]]:
        return self.triangle[:numRows]
        
        