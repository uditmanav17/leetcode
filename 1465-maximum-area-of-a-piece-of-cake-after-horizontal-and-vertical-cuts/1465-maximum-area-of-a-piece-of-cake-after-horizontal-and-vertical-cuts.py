class Solution:
    def maxArea(self, h: int, w: int, 
                horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        horizontalCuts.sort()
        
        verticalCuts.extend([0, w])
        verticalCuts.sort()
        
        # print(horizontalCuts, verticalCuts)
        
        max_h = max_w = 0
        for idx in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[idx] - verticalCuts[idx - 1])
            
        for idx in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[idx] - horizontalCuts[idx - 1])
            
        return (max_w * max_h) % (10**9 + 7)
            
        
        