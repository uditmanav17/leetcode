class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        for num in [tops[0], bottoms[0]]:
            if all(num in (a, b) for a, b in zip(tops, bottoms)):
                # return min(tops.count(num), bottoms.count(num))
                return len(tops) - max(tops.count(num), bottoms.count(num))
            
        return -1
                
                    
                    