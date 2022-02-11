class Solution:
    def intervalIntersection(self, firstList: List[List[int]], 
                             secondList: List[List[int]]) -> List[List[int]]:
        
        p1 = p2 = 0
        ans = []
        
        while p1 < len(firstList) and p2 < len(secondList):
            start_1, end_1 = firstList[p1]
            start_2, end_2 = secondList[p2]
            
            start = max(start_1, start_2)
            end = min(end_1, end_2)
            
            if start <= end:
                ans.append([start, end])
            
            if end_1 < end_2:
                p1 += 1
            else:
                p2 += 1
                
        return ans
