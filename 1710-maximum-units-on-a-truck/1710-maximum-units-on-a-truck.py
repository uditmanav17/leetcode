class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        units = 0
        
        for n_box, n_units in boxTypes:
            boxes_cap = min(n_box, truckSize)
            truckSize -= boxes_cap
            units += (boxes_cap * n_units)
            
            if truckSize == 0:
                break
                
        return units
