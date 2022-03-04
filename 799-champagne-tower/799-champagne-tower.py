# from pprint import pprint as pp

class Solution:
    def champagneTower(self, poured: int, 
                       query_row: int, 
                       query_glass: int) -> float:
        
        l = [[poured]]
        
        for row in range(query_row):
            next_l = [0] * (len(l[-1]) + 1)
            prev_row = l[-1]
            
            for idx, prev_row_liq in enumerate(prev_row):
                liquid_split = (prev_row_liq - 1) / 2
                if liquid_split < 0:
                    continue 
                    
                next_l[idx] += liquid_split
                next_l[idx + 1] += liquid_split
                
            l.append(next_l)
        
        # pp(l)
        
        return min(1, l[query_row][query_glass])
        