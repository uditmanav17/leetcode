class Solution:
    def __init__(self):
        self.pascal = [[1], [1,1]]
        
        while len(self.pascal) < 30:
            prev_row = self.pascal[-1]
            curr_row = [0] * (len(prev_row) + 1)
            curr_row[0] = curr_row[-1] = 1
            for idx in range(1, len(curr_row) - 1):
                curr_row[idx] = prev_row[idx-1] + prev_row[idx]
            self.pascal.append(curr_row[:])
            
    def generate(self, numRows: int) -> List[List[int]]:
        return self.pascal[:numRows]
        